# Trajectory v2: Revise a Scanned Lease Restriction Packet into a Usable Internal Summary

**User:** Andrew (municipal community development coordinator)
**Tools available:** `nano-pdf`, `humanizer`, `word-docx`
**Goal:** Turn a messy scanned redevelopment-authority disposition packet into a concise
internal summary with deadlines, obligations, ambiguities, and follow-up questions for
counsel — without giving legal advice.
**Turn count:** 14 (alternating user / assistant; first-person human dialogue only — no
tool-call JSON blocks)

---

## Turn 1 — Andrew

Okay, I'm going to be straight with you — I have a 4 o'clock check-in with our deputy
director and I just got handed a 22-page scanned packet on a redevelopment parcel I've
never seen before. The scan is sideways on half the pages and somebody used a highlighter
that bled through to the back. I don't need a law review article. I need a clean internal
summary I can actually brief from. The file is `eastside_block_7_disposition.pdf`. Can you
take a swing at it?

## Turn 2 — Assistant

Yes, and I'll be careful to keep this as an internal working summary and not legal
advice — I know that's the line you have to stay on. I'm going to start by running it
through OCR with `nano-pdf` so we're working off real text instead of squinting at a
sideways scan, and I'll auto-rotate the pages that came in flipped. Once I see how clean
the extraction is, I'll decide whether we need to push it through `humanizer` to fix
OCR garbage before I summarize anything.

Quick read on what came out: 22 pages, average OCR confidence around 68% (so, noisy),
five pages were rotated 90° or 180° and got auto-corrected, and the highlighter bleed-
through is showing up as smudges on pages 9, 13, and 17 — those came back as low
confidence. The packet looks like it's actually three documents stapled together: a
Disposition and Development Agreement, a Recorded Declaration of Use Restrictions, and a
short Lease Rider for a ground-floor commercial space. Want me to clean it up first, or
do you want a 30-second "what am I looking at" before I burn any more cycles?

## Turn 3 — Andrew

30 seconds first. If this thing is actually three documents I want to know that going
into the meeting. Tell me what each one is, when it was signed, and who the players are.

## Turn 4 — Assistant

Three documents, in order:

1. **Disposition and Development Agreement (DDA)** — between the **Eastside Redevelopment
   Authority** (seller/grantor) and **Maple & Vine Partners, LLC** (developer). Executed
   **June 8, 2011**. Covers the sale of Block 7 for a mixed-use redevelopment with an
   affordable-housing component.
2. **Declaration of Use Restrictions** — recorded against the Block 7 parcels on
   **June 14, 2011** (six days after the DDA). Runs with the land. This is the document
   that actually binds future owners.
3. **Ground-Floor Commercial Lease Rider** — between Maple & Vine Partners as landlord
   and a then-tenant called **"Cornerstone Café & Roastery, LLC."** Dated **March 2,
   2014**, three years after the DDA. This one is a sub-document — it doesn't bind the
   parcel, it binds whoever is currently leasing the ground-floor commercial bay.

Practical implication for your 4 o'clock: if your deputy director asks "what's actually
restricting the property going forward," the answer is the **Declaration**, not the DDA
and not the café lease. The DDA mostly performed itself once the sale closed. The café
lease is interesting but probably stale — that tenant may not even be there anymore.
Worth confirming.

## Turn 5 — Andrew

That's exactly the framing I needed. Cornerstone closed two years ago, so yeah, the café
rider is probably moot but I want it flagged anyway. Clean the OCR up and give me
deadlines next.

## Turn 6 — Assistant

Cleaning it now with `humanizer` — I told it to preserve legal terms verbatim, fix line
breaks from the column layout, and **flag uncertain spans rather than guess**. That last
bit matters here because of the highlighter bleed: there are at least four places where
the OCR can't decide between two readings, and I'd rather show those to you as
ambiguities than silently pick one.

Here are the date-driven items, sorted by which document they live in:

**From the Declaration of Use Restrictions (the one that runs with the land):**
- **Affordability term: 30 years from the recording date**, so it runs through **June 14,
  2041**.
- **Annual income certification report** to the Redevelopment Authority — due **April 30
  each year** (could also be read as **April 20**; flagged).
- **Notice of any change in ownership** — required **within 15 days** of recording.
- **Default cure period — 45 days** from written notice (this one reads cleanly).

**From the DDA:**
- **Construction completion deadline:** originally **December 31, 2013**. There's a
  handwritten margin note that looks like it says "ext. to 6/30/14" — flagged, can't
  confirm without the certified copy.
- **Reverter trigger:** if construction wasn't completed by the deadline, the Authority
  had the right to take title back. That window is now closed historically, but if there
  was a missed milestone in 2013–14 there could be a lurking question. Flagged.

**From the café lease rider (probably moot, but listed anyway):**
- 10-year initial term, 2014–2024 — already expired by its own terms.
- Two 5-year renewal options — only exercisable by written notice 180 days before
  expiration.

## Turn 7 — Andrew

Good. Obligations now. Group them by who has to do what — and please call out anything
that survives a sale, because the rumor is this parcel may change hands later this year
and my deputy is going to ask.

## Turn 8 — Assistant

Grouped by responsible party, with a survives-sale note where it applies. Plain language,
no editorializing.

**Maple & Vine Partners, LLC (current owner) must:**
- Maintain **at least 25% of the residential units at or below 60% AMI** for the full
  30-year term. **Survives sale** — runs with the land, binds successors.
- Submit the **annual income certification report** to the Redevelopment Authority every
  year. **Survives sale** — the obligation transfers to whoever owns the parcel.
- Provide **15 days' written notice of any ownership change**, including the buyer's
  contact and a recordable assumption agreement. **Survives sale** by definition.
- Keep the on-site community room available to neighborhood groups at no charge — minimum
  **20 hours per month**. **Survives sale.**
- Carry property insurance naming the Authority as additional insured. **Survives sale.**
- Pay all real estate taxes, assessments, and special districts levied on the parcel.
  **Survives sale.**

**Eastside Redevelopment Authority must:**
- Provide written notice and a **45-day cure period** before declaring default.
- Record any release, modification, or estoppel of the restrictions.
- Process annual reports and respond within a "reasonable time" (undefined — flagged).

**Cornerstone Café (under the lease rider, almost certainly moot):**
- Operate as a coffee/food establishment during posted hours, maintain the storefront
  windows, etc. **Does not survive a sale of the parcel** — it's a tenancy obligation,
  not a covenant. Listed for completeness only.

The TL;DR for your deputy director: **everything in the Declaration follows the parcel
to a new owner.** The buyer doesn't get a clean slate. That is by far the most important
sentence in this whole packet.

## Turn 9 — Andrew

That's the sentence I was looking for. Hit me with the use restrictions and then the
ambiguities. I want the ambiguities long and detailed — I'd rather walk in over-prepared
on the sketchy parts.

## Turn 10 — Assistant

**Use restrictions on Block 7:**
- **Mixed-use only** — ground-floor commercial, residential above. No conversion to
  single-use without prior written consent of the Authority.
- **No conversion** of restricted affordable units to market-rate during the 30-year term.
- **No short-term rentals** (defined as any rental under 30 days) anywhere on the parcel.
- **No exterior signage** above the second floor without architectural review (the
  architectural review process is referenced but the committee composition is never
  defined — flagged).
- **No demolition** of the historic façade on the south elevation. Restoration must
  follow the Secretary of the Interior's Standards "to the extent feasible" (the phrase
  "to the extent feasible" is doing a lot of work here — flagged).
- **Right of first refusal** in favor of the Redevelopment Authority on any sale of the
  parcel during the 30-year term.

**Ambiguities and risks — the long version, since you asked:**

- **Annual report due date.** Reads as either **April 20** or **April 30** because the
  highlighter bled across the digit. Ten days is enough to matter for a default notice.
  Counsel should pull the recorded original.
- **The handwritten margin note extending the construction deadline.** If that extension
  was never executed as a formal amendment and recorded, there could be an argument that
  the original December 31, 2013 deadline was missed and that the reverter was triggered.
  Almost certainly a non-issue at this point given how much time has passed and the fact
  that the building got built and occupied — but flag it for counsel because if a future
  buyer's title insurer sees that handwritten note, they may ask.
- **"To the extent feasible"** on the historic façade. Undefined, no standard, no
  arbitrator. Could become a fight if a future owner wants to alter the south elevation.
- **Architectural review committee** — referenced in three places, never defined. Same
  pattern we've seen on other Authority deals.
- **"Reasonable time"** for the Authority to respond to annual reports — undefined.
- **Right of first refusal mechanics.** The clause says the Authority gets a ROFR on any
  sale, but it doesn't specify (a) the notice period, (b) how the price is set when the
  Authority exercises, or (c) whether a related-party transfer counts as a "sale." Big
  gap. Definitely flag for counsel before any rumored sale gets serious.
- **Affordability monitoring fee.** Section 8.4 references an "annual monitoring fee
  payable to the Authority" but the dollar amount is on a referenced **Schedule C** that
  is **not in this packet**. We should ask the Authority for Schedule C directly.
- **The café lease rider.** Even if Cornerstone is gone, if a successor tenant moved in
  under an assignment of that rider, some of those terms might still be live. Worth a
  one-line confirmation.
- **Reverter language in the DDA.** Reads as either **"shall"** revert or **"may"**
  revert depending on which clean-up of the OCR you trust. Big legal difference. Flagged
  hard.

## Turn 11 — Andrew

Perfect, that's exactly the level of paranoia I wanted. Give me the follow-up questions
for counsel — phrase them as questions, like last time. I'll forward them to the city
attorney's office tonight so they're queued up before the parcel changes hands.

## Turn 12 — Assistant

Drafted as questions, neutral phrasing, no embedded conclusions. I numbered them so the
attorney's office can respond inline.

1. Can you pull the recorded Declaration of Use Restrictions from the county recorder so
   we can confirm (a) the exact recording citation, (b) whether the annual income
   certification report is due **April 20** or **April 30**, and (c) whether the DDA's
   reverter language reads as "shall" or "may"?
2. Was the Disposition and Development Agreement's construction completion deadline
   formally extended from December 31, 2013 to June 30, 2014 by a recorded amendment, or
   does the only evidence of that extension live in a handwritten margin note? If only
   the margin note exists, does that create any reverter exposure that a future buyer's
   title insurer would flag?
3. The Declaration's right of first refusal in favor of the Redevelopment Authority does
   not specify a notice period, a pricing mechanism, or whether related-party transfers
   are "sales." How should the city interpret that ROFR if Maple & Vine attempts a sale
   or related-party transfer this year?
4. Section 8.4 references an annual monitoring fee payable to the Authority on a
   Schedule C that is not in our packet. Can you obtain Schedule C directly from the
   Authority and confirm the current fee amount and any escalators?
5. The historic façade restriction requires compliance with the Secretary of the
   Interior's Standards "to the extent feasible." Has the Authority ever taken a
   position on what "feasible" means in practice on Block 7, and is there any prior
   written guidance we should be reading?
6. The architectural review committee referenced in the Declaration is never defined.
   Has it ever been constituted, and what process should the city follow if a successor
   owner proposes exterior changes?
7. The Cornerstone Café lease rider's initial term expired in 2024. Was that lease
   assumed, assigned, or terminated, and does any successor tenant currently operate
   under any of its terms?
8. If Block 7 changes hands later this year, what specific instruments should the city
   require at closing — recordable assumption of the Declaration, estoppel from the
   Authority, updated insurance certificates — to keep the affordability covenant clean
   for the remaining term through 2041?

## Turn 13 — Andrew

These are gold. Package the whole thing as a `.docx`, call it
`block7_internal_working_summary.docx`, put my name on it as preparer, today's date,
disclaimer at the very top — and please do **not** put any "you must" or "you are
required to" language in the body. I'll get burned if this gets forwarded and somebody
reads it as advice. Bullets only, no paragraphs.

## Turn 14 — Assistant

Generating the `.docx` now with `word-docx`. Disclaimer goes on the first page, your name
as preparer, dated today. Bullets only — I went through the body once more and rewrote
anything that read like a directive into neutral framing ("the document states," "the
Declaration appears to require," "counsel should confirm whether"). Section order
matches what we walked through:

1. Internal Use Only — Not Legal Advice (top of page 1, in a box so it's hard to miss)
2. Document Identification — three documents, dates, parties
3. Key Deadlines — split by which document each one comes from
4. Ongoing Obligations — grouped by responsible party, with **survives-sale** notes
5. Use Restrictions on Block 7
6. Risks and Ambiguities — the long version you asked for
7. Follow-Up Questions for Counsel — numbered, phrased as questions
8. Document Provenance — short note that this summary was built from a noisy OCR pass on
   a scanned packet, that three pages had highlighter bleed-through, and that the
   recorded originals should be obtained from the county before relying on any specific
   date or word choice.

Three pages, ~720 words, saved as `block7_internal_working_summary.docx`. Two things I'd
flag before you forward it:

- I deliberately kept the "shall vs. may" reverter ambiguity in the body rather than
  resolving it. If counsel comes back with the certified copy, you can search-and-replace
  the flag in one place.
- The **survives-sale** notes in the Obligations section are the part your deputy
  director will care about most. If you want, I can also generate a one-pager that's
  literally just "what transfers to a new owner of Block 7" — useful as a separate
  handout if the rumored sale gets real.

Otherwise this should be ready for your 4 o'clock. Good luck in there.

---

## End of trajectory v2
**Total turns:** 14 (within the requested 12–16)
**Format:** First-person human dialogue only, no tool-call JSON blocks; tool usage is
described in natural language as the assistant explains what it's doing.
**Tools exercised:** `nano-pdf` (OCR with auto-rotate), `humanizer` (clean OCR with
preserved legal terms and flagged uncertain spans), `word-docx` (final structured
internal summary with disclaimer).
**Distinct from v1:** different parcel (Block 7 vs Parcel 4471), different document mix
(DDA + Declaration + Café Rider vs Declaration + Ground Lease Rider), different time
pressure (4 o'clock briefing), different deputy-director-facing framing (survives-sale
emphasis), different ambiguities (highlighter bleed, "shall vs. may" reverter, missing
Schedule C, handwritten margin extension).
