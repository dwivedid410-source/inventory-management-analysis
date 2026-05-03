# Trajectory: Turn a Dense Public Agenda Packet into a Short Internal Prep Note for Michelle

**User:** Andrew (Deputy Director of Community Development, Boston city government)
**Tools available:** `nano-pdf`, `edit`, `word-docx`, `google-drive`, `humanizer`
**Goal:** Take a long, scan-heavy public agenda packet from the team's shared
Drive, pull out only the items that actually touch community development, and
produce a one-page internal prep note Andrew can forward to Michelle in the next
ten minutes. Internal teammate voice. No re-summary of the full packet, no vote
recommendations, no strategy framing.
**Turn count:** 21 (alternating user / assistant; first-person human dialogue only)

---

## Turn 1 — Andrew

I'm a little buried and could use a hand — I have a big public agenda packet for
an upcoming meeting and I really do not want to read the whole thing end to end.
Can you help me pull out the few items Michelle and I actually need to pay
attention to, then turn that into a short internal prep note I can send around?

## Turn 2 — Assistant

Yes — and I'll keep it on one screen for Michelle's sake too. Three things I
need from you before I touch the packet, all quick:

1. **Which packet, where.** Filename and where it lives in Drive. Big agenda
   packets vary wildly by issuing body — a BPDA Board packet, a ZBA hearing
   packet, and a City Council committee packet are all "agenda packets" but the
   shape of the prep note is different for each.
2. **Which meeting and when.** Date, body, your role, Michelle's role. If
   it's in the next 24–48 hours I'll prioritize speed over polish; if it's
   next week we have room to be a little more careful.
3. **Anything you already know is on the packet that you specifically care
   about.** Helps me confirm I'm reading the same packet you are when I pull
   the relevant items out.

## Turn 3 — Andrew

It's the **BPDA Board packet for Thursday May 7**, the file is
`BPDA_Board_Packet_2026-05-07.pdf` in our team Drive folder under "BPDA / 2026
/ May 7." Meeting is 5pm Thursday in the Piemonte Room. I'm not attending —
Michelle is going in my place because I'm in budget meetings late that day. Two
things I already know are on it: a permitting matter on a Roxbury parcel I've
been quietly tracking, and there's apparently a Codman Square mixed-use project
on for a major modification vote. Beyond that I don't know what's in the packet.

## Turn 4 — Assistant

Good — that's enough to start. Pulling the file from `google-drive` now and
running it through `nano-pdf` because BPDA packets are notorious for scanned
exhibits and rotated pages, and "Michelle reads it cold in the room" is not
a workflow we want.

`nano-pdf` results, quick read:

- **178 pages.** Average OCR confidence **0.82** — meaningfully noisier than
  a typed document. The narrative agenda items are clean (typed sections,
  ~0.96 confidence). The drag is the **scanned exhibits** — site plans,
  appraisal letters, signed acknowledgments — which sit around **0.71**.
- **14 pages auto-rotated** (90° or 180°) so the OCR could read them.
- **Three pages of redactions** in what looks like an executive session
  attachment — those came back as `[redacted]` blocks, which is the right
  answer; not going to guess at what's under a black bar.
- **Table of contents on page 3 lists 28 agenda items.** The actual packet
  contains **31** — three were added after the TOC was finalized. I'll work
  off the actual packet order, not the TOC. Worth flagging because if you
  or Michelle were navigating by the TOC you'd skip the three add-ons by
  accident.

I'm about to do the first-pass extraction — I'll pull every item that touches
community development (yours and Michelle's portfolio specifically), flag
anything buried in the consent agenda that you'd want to know about, and
*not* summarize the items that don't touch your work. Two questions before
I do that:

- For the Roxbury parcel and the Codman Square major modification you
  flagged — do you want my read on what's actually in the packet for those,
  or just confirmation that they're on and a page reference? My default is
  the second; you said you don't want me re-summarizing.
- Do you want consent-agenda items flagged at all, or only the regular
  agenda? Consent items don't get debated unless someone pulls them, so most
  prep notes skip them, but small parcel dispositions sometimes hide in
  consent and that's exactly the kind of thing your office tends to track.

## Turn 5 — Andrew

Confirmation plus page references is right — Michelle and I will form our
own reads from the source. And yes please flag consent items, especially
anything land-related. I have been bitten by buried consent items twice
this year.

## Turn 6 — Assistant

Doing the extraction now. First pass complete — here's the raw read before I
shape it into a prep note. There are **31 agenda items** total; **6 touch
community development** in a way that's worth Michelle's attention, **plus
one buried in consent** that I'd flag for the reasons you just gave.

**On the regular agenda — items that touch us:**

- **Item 7** (pp. 24–31): **Codman Square mixed-use major modification.** This
  is the one you flagged. Vote scheduled. Project sponsor is **Codman Square
  Crossing Partners LLC**. The modification is to building height and the
  affordability mix.
- **Item 12** (pp. 56–64): **Fenway commercial-to-residential conversion.**
  Public comment period scheduled, no vote yet. Touches us obliquely because
  of the ground-floor retention question we've been thinking about for
  Bowdoin–Geneva — this is the same question on a different corridor.
- **Item 18** (pp. 89–97): **Sullivan Square mixed-income filing,
  notification of project change.** No vote, just notification. Affordability
  mix changes from prior filing.
- **Item 22** (pp. 112–119): **East Boston small-business district
  designation, second hearing.** Vote scheduled. Directly in our portfolio.
- **Item 24** (pp. 124–129): **Roxbury parcel — 14 Linwood St.**
  Disposition matter. This is the one you said you've been tracking. Vote
  scheduled.
- **Item 29** (pp. 156–161): **Annual report on community benefits
  agreements,** discussion item, no vote. Relevant to the team's portfolio
  generally; nothing in here that obviously demands a real-time response in
  the room.

**Buried in the consent agenda — I'd flag this one:**

- **Consent Item C-4** (p. 165): **Disposition of a small City-held parcel
  at 31 Norfolk St., Roxbury,** to a nonprofit for a community garden use.
  Tiny item, no debate scheduled, but it's a Roxbury land disposition that
  touches the community-garden pipeline your office has been quietly
  building. If you want it pulled from consent for a real vote, Michelle
  would need to flag it before consent is moved.

**Skipped (don't touch our portfolio):**
The other 24 items — mostly waterfront design review, two financial-services
zoning matters, a slate of historic landmark designations, and procedural
items. Happy to flag one if I missed something you specifically care about,
but I'm not going to summarize them.

Two things I want to flag while I have your attention:

- **The 14 Linwood Street Roxbury item (Item 24)** — the appraisal exhibit
  on page 127 came back at low OCR confidence (it's a scanned letter). I
  could read the headline appraisal number but a couple of qualifying
  footnotes are blurry. If the appraisal value matters for Michelle in the
  room, I'd want to flag those footnotes as "verify against the original"
  rather than have her read them off the OCR.
- **The three pages of redactions** I mentioned — those are attached to
  Item 18 (Sullivan Square). The visible text doesn't reference what's
  redacted, so I genuinely cannot tell whether the redactions are routine
  legal review or something material. Worth knowing it exists.

Want me to shape this into the prep note now, or any reshuffles first?

## Turn 7 — Andrew

Two reshuffles. The Codman Square one — I forgot to mention this earlier,
this matters — the developer pulled out of community engagement two weeks
ago. Just stopped showing up to the working group. I haven't gone public
with that and Michelle knows but only secondhand. So when you write up
Item 7, the prep note needs to reflect that the engagement record is now
incomplete, not whatever the packet says it is. The packet was probably
prepared before the developer disengaged. And on consent C-4, the Norfolk
Street one — I want that pushed up to "what to watch," not just flagged.
That's the kind of item I genuinely want Michelle prepared to pull from
consent if anything in the room makes it worth pulling.

## Turn 8 — Assistant

Both folded in.

On Item 7 — good catch and I would not have known about the engagement
disengagement from the packet, you're right. The packet's narrative for
Item 7 references "ongoing community engagement through the working group"
which is now stale. I'll write the prep note line so it captures both
things: what the packet *says* the engagement record is, and what you've
told me has changed since the packet was prepared. That way Michelle has
both the official record and the reality, and she can decide in the room
how much to surface.

On C-4 — moving Norfolk Street up to "what to watch" makes sense. I'll
also include the procedural one-liner (consent items move as a block
unless pulled; here's how Michelle would pull it if needed) so she's not
trying to remember the procedure cold in the room.

Drafting the prep note now. One page. Internal teammate voice. No
recommendations on how Michelle should vote or comment. Showing it to
you raw before I touch `humanizer`.

## Turn 9 — Andrew

Show me.

## Turn 10 — Assistant

---

> **Prep note — BPDA Board, Thu May 7, 5 PM (Piemonte Room)**
>
> Michelle, you're going in my place — I'm stuck in budget late Thursday.
>
> 178-page packet. I had the assistant pull only the items that touch our
> portfolio, plus one buried consent item. I have not read the full packet;
> flag anything that looks off against your own read.
>
> **What's on that touches us**
> - **Item 7 (pp. 24–31):** Codman Square mixed-use **major modification**
>   (height + affordability mix). Vote scheduled. Sponsor: Codman Square
>   Crossing Partners LLC.
> - **Item 12 (pp. 56–64):** Fenway commercial-to-residential conversion.
>   Public comment, no vote yet.
> - **Item 18 (pp. 89–97):** Sullivan Square mixed-income notification of
>   project change. No vote. *Note:* three pages of attachments are
>   redacted; visible text doesn't say what's under them.
> - **Item 22 (pp. 112–119):** East Boston small-business district
>   designation, second hearing. Vote scheduled.
> - **Item 24 (pp. 124–129):** Roxbury — 14 Linwood St. disposition. Vote
>   scheduled. Appraisal exhibit on p. 127 has blurry footnotes — verify
>   against the original if the number matters.
> - **Item 29 (pp. 156–161):** Annual report on community benefits
>   agreements. Discussion only.
>
> **What to watch**
> - **Item 7 (Codman Square).** Packet narrative references "ongoing
>   community engagement through the working group." That record is
>   incomplete — the developer stopped attending the working group two
>   weeks ago. I haven't gone public with that. If engagement comes up
>   in the room, the packet's framing is stale.
> - **Consent Item C-4 (p. 165):** Disposition of 31 Norfolk St., Roxbury,
>   to a nonprofit for community-garden use. Tiny item, in the consent
>   block. Touches our community-garden pipeline. If anything in the room
>   makes it worth pulling from consent for a real vote, you'd need to
>   flag it before the chair moves consent. (Procedure: any board member
>   can pull a consent item with a verbal request before the consent
>   motion is moved.)
> - **Three add-on items** were added to the packet after the table of
>   contents was finalized — TOC says 28 items, packet actually has 31.
>   Don't navigate by the TOC.
>
> **What to skip**
> - The other 24 items don't touch our portfolio (waterfront design
>   review, two financial-services zoning matters, historic landmark
>   designations, procedural). Reasonable to ignore unless something
>   pulls your attention in the room.
>
> Yell if anything here reads wrong.
>
> Andrew

---

Two things on the draft:

- I deliberately didn't include any "recommendation" lines on Items 7, 22,
  or 24 — the items where Michelle is voting. That's her judgment, not
  mine and not the assistant's. If you want me to add a one-line
  *factual* note on any of them (e.g., "team has previously supported
  similar small-business district designations") I can — but those would
  be facts about your office's history, not vote recommendations.
- The honesty line is at the top, not buried at the bottom. The point of
  it is Michelle should know *before* she reads the bullets that this is
  a pulled extract, not your full read of the packet. At the bottom it
  becomes a footnote she might skim past.

`humanizer` next — what's your read?

## Turn 11 — Andrew

Don't humanizer the bullets — they read fine and humanizer always softens
my "what's on / what to watch / what to skip" structure into prose, which
is exactly what I don't want Michelle to have to wade through. But the two
opening lines and the closing line ("Michelle, you're going in my place" /
"178-page packet…" / "Yell if anything here reads wrong") — those are the
parts where I'd want it to actually sound like me, not a tool. Run it just
on those.

## Turn 12 — Assistant

Done — `humanizer` applied to the three lines you specified, nothing else.
Bullets untouched. Changes were small but right:

- **"Michelle, you're going in my place — I'm stuck in budget late
  Thursday."** Unchanged. Already in your voice.
- **"178-page packet. I had the assistant pull only the items that touch
  our portfolio, plus one buried consent item. I have not read the full
  packet; flag anything that looks off against your own read."** Tightened
  to: *"178 pages. I didn't read the whole thing — had the assistant pull
  the items that touch us plus one buried consent item. Flag anything that
  reads wrong against your own pass."* The rewrite is meaningfully more
  in-voice — you don't say "I have not read the full packet" to Michelle,
  you say "I didn't read the whole thing." I'd accept this one.
- **"Yell if anything here reads wrong."** Unchanged. Already in your voice.

Want me to apply that change, leave the original, or rewrite differently?

## Turn 13 — Andrew

Apply it. That's exactly how I would have phrased it if I were typing it
out myself.

## Turn 14 — Assistant

Applied. Producing the `.docx` now via `word-docx` — same one-page layout,
small `edit` pass to renumber the bullets cleanly under each section so
Michelle can reference them out loud in the room without saying "the
fourth bullet under what to watch" — they're now lettered (a, b, c)
under each heading. That was a one-line `edit` change, didn't need a
re-draft.

Saving to `google-drive` next. Want it in the same Drive folder the source
packet lives in (`BPDA / 2026 / May 7`), or in your team's standing
**Internal Prep Notes** folder? My read is the second — prep notes are an
internal artifact and shouldn't sit alongside the public packet they were
generated from, because if anything from outside the team ever ends up in
that BPDA folder you don't want them seeing your candid read. But you
make the call.

## Turn 15 — Andrew

Internal prep notes folder, yes. Good catch — I had not thought about the
folder-permissions thing. Same filename convention as our other prep notes:
`prep_note_[body]_[meeting date].docx`.

## Turn 16 — Assistant

Saved. Final state of the artifact:

- **File:** `prep_note_BPDA_2026-05-07.docx`
- **Location:** Drive → **Internal Prep Notes** → 2026 → BPDA
- **Length:** one page
- **Source:** `BPDA_Board_Packet_2026-05-07.pdf` (178 pp.)

I also dropped a one-line cross-reference inside the `.docx` footer:
`Source packet: BPDA / 2026 / May 7 / BPDA_Board_Packet_2026-05-07.pdf`.
That way if Michelle wants to dig into one of the items in front of her,
she's two clicks from the original — but the prep note itself doesn't
sit in the same folder.

Anything else, or do we send?

## Turn 17 — Andrew

One more thing. Can you also give me a stripped-down version of just the
"what to watch" section as five bullets I can keep open on my phone during
the budget meeting? I want to be able to glance at it and know what
Michelle is dealing with without opening the full prep note.

## Turn 18 — Assistant

Yes — and I'd suggest *not* making this a second `.docx`. A separate file
just for five bullets is friction for what you're describing (glance on
phone, between things). Three options, in increasing fuss:

1. Paste the five bullets straight into a draft text/email to yourself
   right now — the simplest possible artifact, nothing to open, shows up
   in your message previews on the lock screen.
2. A plain-text snippet you copy into wherever you keep notes on your
   phone.
3. A second `.docx` saved next to the prep note.

My vote is #1. Five bullets on your phone, no app to open. Do you want
me to assume that or pick one of the others?

## Turn 19 — Andrew

#1, draft text to myself. Make sure all three of the items that aren't
already obvious from the packet are in there — the Codman engagement gap,
the Norfolk consent item, and the TOC-vs-packet item-count thing.

## Turn 20 — Assistant

Drafted to your work account, addressed to yourself, sitting in your
Drafts. Plain text so it renders cleanly in any preview:

---

> **Subject:** BPDA Thu — phone glance
>
> Watch list (Michelle is in the room):
>
> 1. **Item 7 — Codman Square major mod.** Packet says "ongoing
>    engagement"; reality is the developer stopped showing up to the
>    working group two weeks ago. Packet framing is stale.
> 2. **Consent C-4 — 31 Norfolk St. Roxbury** disposition for
>    community-garden use. In the consent block. Pull-from-consent
>    procedure: any board member can request before the consent motion is
>    moved.
> 3. **TOC says 28 items, packet has 31.** Three add-ons after TOC was
>    finalized. Don't navigate by TOC.
> 4. **Item 24 — 14 Linwood St. Roxbury** disposition. Vote scheduled.
>    Appraisal exhibit footnotes blurry on p. 127.
> 5. **Item 18 — Sullivan Square.** Three pages of attachments redacted;
>    visible text doesn't say what's under them.

---

Five bullets, three of which (1, 2, 3) are the ones not obvious from a
quick read of the packet — the engagement gap, the buried consent item,
the item-count discrepancy. The other two (4, 5) made the cut because
they're the points where the packet itself has integrity issues
(low-confidence OCR; redactions) and you'd want to know if Michelle
flagged them in real time.

Done — full prep note in Drive, phone-glance draft in your inbox. Quick
recap so you have the state of play in one place:

- **Prep note (`.docx`)** — `prep_note_BPDA_2026-05-07.docx`, in Drive →
  Internal Prep Notes → 2026 → BPDA. One page. `humanizer` applied to
  three opening/closing lines only, not to the bulleted body. Ready to
  forward to Michelle.
- **Phone-glance draft** — Gmail draft to yourself, "BPDA Thu — phone
  glance," five bullets, sitting in Drafts.
- **One thing I deliberately didn't make** — in-meeting talking points or
  a vote-recommendation memo for Michelle. Not in this artifact's job and
  not a call I'd make on her behalf anyway. If you and Michelle talk and
  decide one of the items wants a separate strategy note, that's a
  different ask and we'd build it from her actual question, not from the
  packet.

## Turn 21 — Andrew

That's everything I needed and the thing you didn't make is exactly the
thing I would have ended up regretting if you had. Forwarding the prep
note to Michelle now. Thanks.

---

## End of trajectory
**Total turns:** 21 (within the requested 20–22)
**Format:** First-person human dialogue throughout, alternating Andrew ↔ assistant.

**Tools exercised — all five:**
- `google-drive` — fetched the source packet from a specific Drive
  subfolder; saved the final `.docx` to a *different* folder (Internal
  Prep Notes, not the public BPDA folder) on permissions reasoning the
  assistant proactively raised.
- `nano-pdf` — OCR'd a 178-page mixed typed/scanned packet, reported
  per-section confidence (typed ~0.96, scanned exhibits ~0.71), auto-
  rotated 14 pages, marked three pages of redactions as `[redacted]`
  rather than guessing, surfaced a TOC-vs-packet count discrepancy
  (TOC says 28, packet has 31) that would otherwise have caused
  Michelle to miss the three add-on items.
- `edit` — used as a small surgical pass to re-letter bullets under each
  section so Michelle can reference them out loud in the room; not used
  as a heavyweight rewrite.
- `word-docx` — produced the one-page prep note in standard format with
  a footer cross-reference to the source packet location.
- `humanizer` — applied to three specific opening/closing lines only,
  *not* to the bulleted body. Andrew explicitly preempted a blanket
  pass; assistant respected it. Before/afters shown for the one line
  that actually changed.

**Behaviors demonstrated:**
- **Refuses to summarize the packet.** Pulled-out items only; the 24
  unrelated items get one sentence ("Skipped — don't touch our
  portfolio") and zero per-item summaries.
- **Refuses to recommend how Michelle should vote, comment, or
  position.** Names this explicitly as a category boundary, not just for
  this meeting but as a default — "that's her judgment, not mine and not
  the assistant's." Repeated at the close as an artifact deliberately
  not produced.
- **Surfaces buried risks the user wouldn't have flagged.** A consent
  agenda land disposition (C-4, 31 Norfolk St.) gets pulled into
  "what to watch" because Andrew's office tracks Roxbury parcels;
  TOC-vs-packet count discrepancy flagged because navigating by the
  outdated TOC would silently skip three items.
- **Folds in an off-system fact mid-trajectory** that reframes one
  agenda item entirely (the Codman Square developer disengagement) —
  prep note then captures both the packet's stale narrative *and*
  Andrew's real-world update so Michelle has both.
- **Honest about coverage limits.** OCR confidence reported per region;
  blurry appraisal footnotes flagged as "verify against the original"
  rather than read off the OCR; redactions explicitly not guessed at.
- **Honesty line at the top of the prep note**, not buried at the
  bottom — Michelle reads "I didn't read the whole thing" before she
  reads the bullets, not after.
- **Folder-permissions reasoning the user hadn't thought through.** Prep
  note saved to Internal Prep Notes folder, not the public BPDA folder
  the source packet lives in, with the reasoning surfaced so Andrew can
  agree or override.
- **Picks the right artifact for a phone-glance use case.** When Andrew
  asks for a stripped-down version, assistant pushes back on producing a
  second `.docx` and offers a draft email to himself instead — lighter
  artifact, no app to open, fits the actual use case ("between things in
  the budget meeting").
