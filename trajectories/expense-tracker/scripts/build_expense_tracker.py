"""Build the final Simple Expense Tracker workbook.

This script produces `output/expense_tracker.xlsx`, the deliverable
from the trajectory in `../trajectory.md`. The workbook contains:

  - Instructions  : a one-page how-to-use sheet
  - Expenses      : the data entry table (Date, Category, Description,
                    Payment Method, Amount, Notes) formatted as an Excel
                    Table so new rows extend formulas/formatting
                    automatically.
  - Summary       : monthly totals, by-category totals (SUMIF), top
                    category formula, budget vs actual, and a small
                    pie chart.
  - Categories    : the dropdown list backing data validation on the
                    Expenses sheet.

The workbook is intentionally simple: everything is computed with
plain Excel formulas (SUM, SUMIF, SUMIFS, COUNTIF, INDEX/MATCH, IF)
so the user can read and modify it without help.
"""

from __future__ import annotations

import datetime as dt
from pathlib import Path

from openpyxl import Workbook
from openpyxl.chart import PieChart, Reference
from openpyxl.styles import (
    Alignment,
    Border,
    Font,
    PatternFill,
    Side,
)
from openpyxl.utils import get_column_letter
from openpyxl.workbook.defined_name import DefinedName
from openpyxl.worksheet.table import Table, TableStyleInfo
from openpyxl.worksheet.datavalidation import DataValidation


OUTPUT_PATH = Path(__file__).resolve().parent.parent / "output" / "expense_tracker.xlsx"

# ---- styling helpers --------------------------------------------------------

NAVY = "1F3A5F"
LIGHT = "EAF1F8"
ACCENT = "2E7D5B"
WARN = "C0392B"
GREY = "F4F4F4"

THIN = Side(style="thin", color="BFBFBF")
BOX = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)

TITLE_FONT = Font(name="Calibri", size=18, bold=True, color="FFFFFF")
H2_FONT = Font(name="Calibri", size=12, bold=True, color=NAVY)
HEADER_FONT = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
BODY_FONT = Font(name="Calibri", size=11)
BOLD_BODY = Font(name="Calibri", size=11, bold=True)

NAVY_FILL = PatternFill("solid", fgColor=NAVY)
LIGHT_FILL = PatternFill("solid", fgColor=LIGHT)
GREY_FILL = PatternFill("solid", fgColor=GREY)
ACCENT_FILL = PatternFill("solid", fgColor=ACCENT)


def _band(cell, *, fill=None, font=None, align=None, border=BOX, fmt=None):
    if fill is not None:
        cell.fill = fill
    if font is not None:
        cell.font = font
    if align is not None:
        cell.alignment = align
    if border is not None:
        cell.border = border
    if fmt is not None:
        cell.number_format = fmt


# ---- sample data ------------------------------------------------------------

CATEGORIES = [
    "Rent",
    "Groceries",
    "Utilities",
    "Transport",
    "Dining Out",
    "Entertainment",
    "Health",
    "Shopping",
    "Subscriptions",
    "Other",
]

PAYMENT_METHODS = ["Cash", "Debit Card", "Credit Card", "Bank Transfer"]

# A small, realistic month of expenses so the formulas show real numbers.
SAMPLE_ROWS = [
    (dt.date(2026, 5, 1),  "Rent",          "May rent",              "Bank Transfer", 1450.00, ""),
    (dt.date(2026, 5, 2),  "Groceries",     "Weekly shop",           "Debit Card",      82.45, ""),
    (dt.date(2026, 5, 3),  "Dining Out",    "Brunch with Sam",       "Credit Card",     34.10, ""),
    (dt.date(2026, 5, 4),  "Transport",     "Metro card top-up",     "Debit Card",      40.00, ""),
    (dt.date(2026, 5, 5),  "Utilities",     "Electricity bill",      "Bank Transfer",   78.20, ""),
    (dt.date(2026, 5, 6),  "Subscriptions", "Streaming service",     "Credit Card",     14.99, ""),
    (dt.date(2026, 5, 8),  "Groceries",     "Mid-week top-up",       "Debit Card",      26.30, ""),
    (dt.date(2026, 5, 9),  "Entertainment", "Cinema",                "Credit Card",     22.00, ""),
    (dt.date(2026, 5, 10), "Dining Out",    "Pizza night",           "Cash",            18.50, ""),
    (dt.date(2026, 5, 12), "Health",        "Pharmacy",              "Debit Card",      15.75, ""),
    (dt.date(2026, 5, 13), "Transport",     "Rideshare home",        "Credit Card",     12.40, ""),
    (dt.date(2026, 5, 15), "Groceries",     "Weekly shop",           "Debit Card",      94.10, ""),
    (dt.date(2026, 5, 16), "Shopping",      "T-shirts",              "Credit Card",     38.00, ""),
    (dt.date(2026, 5, 18), "Utilities",     "Internet",              "Bank Transfer",   45.00, ""),
    (dt.date(2026, 5, 19), "Dining Out",    "Lunch at work",         "Cash",            12.80, ""),
    (dt.date(2026, 5, 20), "Subscriptions", "Cloud storage",         "Credit Card",      9.99, ""),
    (dt.date(2026, 5, 22), "Groceries",     "Weekend shop",          "Debit Card",      71.65, ""),
    (dt.date(2026, 5, 23), "Entertainment", "Concert ticket",        "Credit Card",     55.00, ""),
    (dt.date(2026, 5, 25), "Transport",     "Fuel",                  "Debit Card",      48.20, ""),
    (dt.date(2026, 5, 27), "Health",        "Gym day pass",          "Cash",            10.00, ""),
    (dt.date(2026, 5, 29), "Other",         "Birthday gift",         "Credit Card",     30.00, ""),
    (dt.date(2026, 5, 30), "Dining Out",    "Family dinner",         "Credit Card",     62.45, ""),
]


# ---- builders ---------------------------------------------------------------

def build_categories_sheet(wb: Workbook) -> None:
    ws = wb.create_sheet("Categories")
    ws["A1"] = "Category"
    ws["B1"] = "Monthly Budget"
    _band(ws["A1"], fill=NAVY_FILL, font=HEADER_FONT, align=Alignment(horizontal="center"))
    _band(ws["B1"], fill=NAVY_FILL, font=HEADER_FONT, align=Alignment(horizontal="center"))

    default_budgets = {
        "Rent": 1450,
        "Groceries": 450,  # bumped from 350 in turn 11 of the trajectory
        "Utilities": 150,
        "Transport": 120,
        "Dining Out": 150,
        "Entertainment": 80,
        "Health": 60,
        "Shopping": 100,
        "Subscriptions": 30,
        "Other": 50,
    }
    for i, cat in enumerate(CATEGORIES, start=2):
        ws.cell(row=i, column=1, value=cat).font = BODY_FONT
        ws.cell(row=i, column=1).border = BOX
        b = ws.cell(row=i, column=2, value=default_budgets.get(cat, 0))
        b.number_format = '"$"#,##0.00'
        b.font = BODY_FONT
        b.border = BOX

    ws.column_dimensions["A"].width = 18
    ws.column_dimensions["B"].width = 18

    ws["D1"] = "Payment Method"
    _band(ws["D1"], fill=NAVY_FILL, font=HEADER_FONT, align=Alignment(horizontal="center"))
    for i, pm in enumerate(PAYMENT_METHODS, start=2):
        c = ws.cell(row=i, column=4, value=pm)
        c.font = BODY_FONT
        c.border = BOX
    ws.column_dimensions["D"].width = 18

    # Named ranges so data validation reads cleanly.
    wb.defined_names["CategoryList"] = DefinedName(
        "CategoryList",
        attr_text=f"Categories!$A$2:$A${len(CATEGORIES) + 1}",
    )
    wb.defined_names["PaymentList"] = DefinedName(
        "PaymentList",
        attr_text=f"Categories!$D$2:$D${len(PAYMENT_METHODS) + 1}",
    )


def build_expenses_sheet(wb: Workbook) -> None:
    ws = wb.create_sheet("Expenses")

    headers = ["Date", "Category", "Description", "Payment Method", "Amount", "Notes"]
    for col, h in enumerate(headers, start=1):
        c = ws.cell(row=1, column=col, value=h)
        _band(c, fill=NAVY_FILL, font=HEADER_FONT, align=Alignment(horizontal="center"))

    for r, row in enumerate(SAMPLE_ROWS, start=2):
        date, cat, desc, pm, amt, notes = row
        ws.cell(row=r, column=1, value=date).number_format = "yyyy-mm-dd"
        ws.cell(row=r, column=2, value=cat)
        ws.cell(row=r, column=3, value=desc)
        ws.cell(row=r, column=4, value=pm)
        ws.cell(row=r, column=5, value=amt).number_format = '"$"#,##0.00'
        ws.cell(row=r, column=6, value=notes)
        for col in range(1, 7):
            cc = ws.cell(row=r, column=col)
            cc.font = BODY_FONT
            cc.border = BOX
            if col == 5:
                cc.alignment = Alignment(horizontal="right")
            elif col in (1, 2, 4):
                cc.alignment = Alignment(horizontal="left")

    last_row = 1 + len(SAMPLE_ROWS)
    table_ref = f"A1:F{last_row}"
    table = Table(displayName="ExpensesTbl", ref=table_ref)
    table.tableStyleInfo = TableStyleInfo(
        name="TableStyleMedium2",
        showRowStripes=True,
        showColumnStripes=False,
    )
    ws.add_table(table)

    widths = {1: 12, 2: 16, 3: 32, 4: 18, 5: 12, 6: 28}
    for col, w in widths.items():
        ws.column_dimensions[get_column_letter(col)].width = w
    ws.row_dimensions[1].height = 22
    ws.freeze_panes = "A2"

    # Data validation: category dropdown + payment method dropdown.
    dv_cat = DataValidation(
        type="list",
        formula1="=CategoryList",
        allow_blank=True,
        showErrorMessage=True,
        errorTitle="Invalid category",
        error="Pick a category from the list (or add it on the Categories sheet).",
    )
    dv_pm = DataValidation(
        type="list",
        formula1="=PaymentList",
        allow_blank=True,
    )
    dv_amt = DataValidation(
        type="decimal",
        operator="greaterThanOrEqual",
        formula1=0,
        allow_blank=True,
        showErrorMessage=True,
        errorTitle="Invalid amount",
        error="Amount must be a number greater than or equal to 0.",
    )
    ws.add_data_validation(dv_cat)
    ws.add_data_validation(dv_pm)
    ws.add_data_validation(dv_amt)
    dv_cat.add(f"B2:B{last_row + 200}")
    dv_pm.add(f"D2:D{last_row + 200}")
    dv_amt.add(f"E2:E{last_row + 200}")


def build_summary_sheet(wb: Workbook) -> None:
    ws = wb.create_sheet("Summary")

    ws.merge_cells("A1:F1")
    title = ws["A1"]
    title.value = "Monthly Expense Summary"
    title.font = TITLE_FONT
    title.alignment = Alignment(horizontal="center", vertical="center")
    title.fill = NAVY_FILL
    ws.row_dimensions[1].height = 32

    ws["A3"] = "Reporting month"
    ws["B3"] = dt.date(2026, 5, 1)
    ws["B3"].number_format = "mmmm yyyy"
    ws["A3"].font = BOLD_BODY
    ws["B3"].font = BODY_FONT

    ws["A4"] = "Last updated"
    ws["B4"] = "=TODAY()"
    ws["B4"].number_format = "yyyy-mm-dd"
    ws["A4"].font = BOLD_BODY
    ws["B4"].font = BODY_FONT

    # KPI cards
    kpis = [
        ("Total spent",       '=SUM(ExpensesTbl[Amount])'),
        ("Number of expenses",'=COUNTA(ExpensesTbl[Amount])'),
        ("Average expense",   '=IFERROR(AVERAGE(ExpensesTbl[Amount]),0)'),
        ("Largest expense",   '=IFERROR(MAX(ExpensesTbl[Amount]),0)'),
    ]
    for i, (label, formula) in enumerate(kpis):
        col = 1 + i * 2  # A, C, E, G... we'll keep it tight: A,B,C,D,E,F
        # Place in a 2x4 grid: row 6 labels / row 7 values, columns A:H
        pass
    # Simpler layout: 4 KPI cards stacked horizontally over A:H
    for i, (label, formula) in enumerate(kpis):
        c1 = 1 + i * 2
        c2 = c1 + 1
        # Merge label across 2 cols, value across 2 cols.
        ws.cell(row=6, column=c1, value=label)
        ws.merge_cells(start_row=6, start_column=c1, end_row=6, end_column=c2)
        v = ws.cell(row=7, column=c1, value=formula)
        ws.merge_cells(start_row=7, start_column=c1, end_row=7, end_column=c2)
        for cell in (ws.cell(row=6, column=c1), ws.cell(row=7, column=c1)):
            cell.alignment = Alignment(horizontal="center", vertical="center")
        ws.cell(row=6, column=c1).fill = NAVY_FILL
        ws.cell(row=6, column=c1).font = HEADER_FONT
        ws.cell(row=7, column=c1).fill = LIGHT_FILL
        ws.cell(row=7, column=c1).font = Font(name="Calibri", size=14, bold=True, color=NAVY)
        if label in ("Total spent", "Average expense", "Largest expense"):
            v.number_format = '"$"#,##0.00'
        else:
            v.number_format = "0"
    ws.row_dimensions[6].height = 22
    ws.row_dimensions[7].height = 28

    # By-category table
    ws["A10"] = "Spending by Category"
    ws["A10"].font = H2_FONT

    headers = ["Category", "Spent", "Budget", "Remaining", "% of Total"]
    for i, h in enumerate(headers, start=1):
        c = ws.cell(row=11, column=i, value=h)
        _band(c, fill=NAVY_FILL, font=HEADER_FONT, align=Alignment(horizontal="center"))

    for i, cat in enumerate(CATEGORIES, start=12):
        ws.cell(row=i, column=1, value=cat)
        ws.cell(row=i, column=2,
                value=f'=SUMIF(ExpensesTbl[Category],A{i},ExpensesTbl[Amount])')
        ws.cell(row=i, column=3,
                value=f'=VLOOKUP(A{i},Categories!$A$2:$B${len(CATEGORIES) + 1},2,FALSE)')
        ws.cell(row=i, column=4, value=f"=C{i}-B{i}")
        ws.cell(row=i, column=5, value=f"=IFERROR(B{i}/$A$7,0)")

        for col in range(1, 6):
            cc = ws.cell(row=i, column=col)
            cc.font = BODY_FONT
            cc.border = BOX
            if col == 1:
                cc.alignment = Alignment(horizontal="left")
            else:
                cc.alignment = Alignment(horizontal="right")
        for col in (2, 3, 4):
            ws.cell(row=i, column=col).number_format = '"$"#,##0.00'
        ws.cell(row=i, column=5).number_format = "0.0%"

    total_row = 12 + len(CATEGORIES)
    ws.cell(row=total_row, column=1, value="Total")
    ws.cell(row=total_row, column=2, value=f"=SUM(B12:B{total_row - 1})")
    ws.cell(row=total_row, column=3, value=f"=SUM(C12:C{total_row - 1})")
    ws.cell(row=total_row, column=4, value=f"=SUM(D12:D{total_row - 1})")
    ws.cell(row=total_row, column=5, value=f"=SUM(E12:E{total_row - 1})")
    for col in range(1, 6):
        cc = ws.cell(row=total_row, column=col)
        cc.font = BOLD_BODY
        cc.fill = LIGHT_FILL
        cc.border = BOX
        if col >= 2 and col <= 4:
            cc.number_format = '"$"#,##0.00'
        if col == 5:
            cc.number_format = "0.0%"
        if col == 1:
            cc.alignment = Alignment(horizontal="left")
        else:
            cc.alignment = Alignment(horizontal="right")

    # Highlight box: top category + over-budget count
    ws.cell(row=total_row + 2, column=1, value="Top spending category").font = BOLD_BODY
    ws.cell(
        row=total_row + 2, column=2,
        value=f'=INDEX(A12:A{total_row - 1},MATCH(MAX(B12:B{total_row - 1}),B12:B{total_row - 1},0))',
    ).font = BODY_FONT

    ws.cell(row=total_row + 3, column=1, value="Categories over budget").font = BOLD_BODY
    ws.cell(
        row=total_row + 3, column=2,
        value=f'=COUNTIF(D12:D{total_row - 1},"<0")',
    ).font = BODY_FONT
    ws.cell(row=total_row + 3, column=2).number_format = "0"

    # Column widths
    widths = {1: 18, 2: 14, 3: 14, 4: 14, 5: 12, 6: 14, 7: 14, 8: 14}
    for col, w in widths.items():
        ws.column_dimensions[get_column_letter(col)].width = w

    # Pie chart of category spend
    pie = PieChart()
    labels = Reference(ws, min_col=1, min_row=12, max_row=total_row - 1)
    data = Reference(ws, min_col=2, min_row=11, max_row=total_row - 1)
    pie.add_data(data, titles_from_data=True)
    pie.set_categories(labels)
    pie.title = "Share of Spending by Category"
    pie.height = 9
    pie.width = 14
    ws.add_chart(pie, f"G10")

    ws.sheet_view.showGridLines = False


def build_instructions_sheet(wb: Workbook) -> None:
    ws = wb.create_sheet("Instructions")

    ws.merge_cells("A1:E1")
    t = ws["A1"]
    t.value = "Simple Expense Tracker — How to Use"
    t.font = TITLE_FONT
    t.fill = NAVY_FILL
    t.alignment = Alignment(horizontal="center", vertical="center")
    ws.row_dimensions[1].height = 32

    steps = [
        ("1.", "Open the Expenses sheet and add one row per expense."),
        ("2.", "Pick a Category and Payment Method from the dropdowns. The dropdowns are driven by the Categories sheet — edit that sheet to add or rename categories."),
        ("3.", "Enter the Amount as a positive number. Negative numbers are blocked."),
        ("4.", "Open the Summary sheet to see totals, by-category spend, budget vs actual, and the share-of-spending pie chart."),
        ("5.", "Set your monthly budget per category in column B of the Categories sheet. The Summary sheet will flag categories that are over budget."),
        ("6.", "To reuse the workbook for a new month, copy the file, then clear the rows under the headers on the Expenses sheet."),
    ]
    for i, (n, txt) in enumerate(steps, start=3):
        ws.cell(row=i, column=1, value=n).font = BOLD_BODY
        c = ws.cell(row=i, column=2, value=txt)
        c.font = BODY_FONT
        c.alignment = Alignment(wrap_text=True, vertical="top")
        ws.merge_cells(start_row=i, start_column=2, end_row=i, end_column=5)
        ws.row_dimensions[i].height = 32

    ws.column_dimensions["A"].width = 5
    for col in ("B", "C", "D", "E"):
        ws.column_dimensions[col].width = 22

    ws.cell(row=10, column=1, value="Formulas used").font = H2_FONT
    formula_rows = [
        ("Total spent",        "=SUM(ExpensesTbl[Amount])"),
        ("Spent per category", "=SUMIF(ExpensesTbl[Category], <category>, ExpensesTbl[Amount])"),
        ("Budget per category","=VLOOKUP(<category>, Categories!A:B, 2, FALSE)"),
        ("Top category",       "=INDEX(<cat range>, MATCH(MAX(<spent range>), <spent range>, 0))"),
        ("Over-budget count",  '=COUNTIF(<remaining range>, "<0")'),
    ]
    for i, (label, formula) in enumerate(formula_rows, start=11):
        ws.cell(row=i, column=1, value=label).font = BOLD_BODY
        c = ws.cell(row=i, column=2, value=formula)
        c.font = Font(name="Consolas", size=10)
        ws.merge_cells(start_row=i, start_column=2, end_row=i, end_column=5)

    ws.sheet_view.showGridLines = False


# ---- main -------------------------------------------------------------------

def main() -> Path:
    wb = Workbook()
    wb.remove(wb.active)

    build_instructions_sheet(wb)
    build_expenses_sheet(wb)
    build_summary_sheet(wb)
    build_categories_sheet(wb)

    wb.active = wb.sheetnames.index("Summary")

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    wb.save(OUTPUT_PATH)
    return OUTPUT_PATH


if __name__ == "__main__":
    out = main()
    print(f"Wrote {out}")
