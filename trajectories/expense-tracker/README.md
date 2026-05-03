# Trajectory — Simple Expense Tracker Spreadsheet

A 21-turn, first-person human/assistant trajectory for the task
**"Build a Simple Expense Tracker Spreadsheet."**

- **Conversation:** [`trajectory.md`](trajectory.md)
- **Build script:** [`scripts/build_expense_tracker.py`](scripts/build_expense_tracker.py)
- **Final workbook:** [`output/expense_tracker.xlsx`](output/expense_tracker.xlsx)

## What the deliverable contains

The generated `expense_tracker.xlsx` has four sheets:

| Sheet         | Purpose |
|---------------|---------|
| Instructions  | One-page how-to and a formulas reference. |
| Expenses      | Data-entry table (`ExpensesTbl`) with Date, Category, Description, Payment Method, Amount, Notes. Validated dropdowns; numeric guard on Amount. |
| Summary       | KPI cards, by-category table (Spent / Budget / Remaining / % of Total), top-category callout, over-budget count, and a pie chart. Opens here on file open. |
| Categories    | Drives the Category and Payment Method dropdowns. Holds per-category monthly budgets. |

Everything is computed with plain Excel formulas (`SUM`, `SUMIF`,
`VLOOKUP`, `INDEX`/`MATCH`, `COUNTIF`, `IFERROR`) so the workbook is
readable without macros.

## Rebuild

```bash
pip install openpyxl
python3 scripts/build_expense_tracker.py
```
