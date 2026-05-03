# Trajectory: Remember My Preferred Format for Reviewing Local Policy News Each Friday

**User:** Andrew (Deputy Director of Community Development, Boston city government)
**Tools available:** `memory`, `news-summary`, `humanizer`, `conversation`
**Goal:** Establish and save a durable default for how the assistant briefs Andrew
on Boston-area local policy news at the end of each week. The session works the
preference out *on a real Friday's news*, not in the abstract, then writes the
calibrated default to memory so future Friday sessions can pick it up cold.
**Turn count:** 21 (alternating user / assistant; first-person human dialogue only)

---

## Turn 1 — Andrew

Can we set a default for how you brief me on local policy news? I keep asking
for basically the same thing and I'd rather not re-explain it every Friday.

## Turn 2 — Assistant

Yes — and the right way to do this is to actually run one with you today, not
just describe a format in the abstract. It's Friday May 1, you have actual
Boston-area policy news from this week sitting in `news-summary` already, and
the calibration session will be sharper if we work off the real thing rather
than a hypothetical.

Plan, three steps:

1. **Quick `conversation` pass** — five short questions to pin down the
   shape. Not twenty. Just the choices that genuinely change the artifact.
2. **Live trial run** — I pull this week's actual Boston-area policy news
   via `news-summary` and produce a brief in the shape we just landed on.
3. **You react to the real example.** Whatever changes that surfaces, we
   fold in. Then I write the calibrated default to `memory` and read it
   back so you can spot anything off before it sticks.

Sound right? If yes I'll start the five-question pass.

## Turn 3 — Andrew

Yes, do it that way. Five questions.

## Turn 4 — Assistant

Five questions, in order. Quick answers are fine — I'm calibrating a default,
not writing your biography.

1. **Length.** Where do you want this to land — one short paragraph, one
   screen of bullets, or longer like a real newsletter? My read of how you
   work is "one screen, no scrolling on the phone," but tell me if I'm
   wrong.
2. **Geography.** Boston city only? Boston-area (Cambridge, Somerville,
   Brookline)? Mass-state-when-it-touches-Boston? National when it
   intersects with city work? I'd rather over-ask than guess and have to
   un-set it later.
3. **Sources.** Do you have outlets you actively trust (*Globe*,
   *CommonWealth*, *Banker & Tradesman*, *Boston Business Journal*, the
   neighborhood blogs, City Council meeting recaps)? Outlets you actively
   distrust? I'll weight pulls accordingly.
4. **Voice.** "Smart staffer's plain-language read," "neutral wire-copy
   summary," or "lightly opinionated brief from someone who knows your
   portfolio"? These produce noticeably different artifacts.
5. **Delivery.** Do you want this to land in your inbox automatically every
   Friday morning, or do you want to summon it when you're ready to read
   it? I'm going to push gently against auto-delivery for the inbox-fatigue
   reason, but it's your call.

## Turn 5 — Andrew

1. One screen, no scrolling. You read me right.
2. Boston city, BPDA, Mass legislature when it touches Boston, MassDOT when
   it touches Boston. Cambridge or Somerville only if it sets a precedent
   I'll get asked about. Skip national entirely — I read national elsewhere
   and I do not want it in this brief.
3. Trust the *Globe* metro desk, *CommonWealth*, *Banker & Tradesman* on
   real estate stuff, *Dorchester Reporter* and *Bay State Banner* on the
   neighborhoods I work in. *Boston Business Journal* is fine but skews
   booster — flag anything from there as such if it shows up. Skip the
   national outlets even when they cover Boston.
4. Smart staffer's plain-language read. Not wire-copy, not opinionated.
5. Summon, don't push. You're right that an auto-Friday email becomes
   background noise within three weeks — I've watched it happen with three
   other newsletters I now archive unread.

## Turn 6 — Assistant

Good — that's enough to do the live trial. Pulling this week's Boston-area
policy news via `news-summary` now, weighted to the outlets you flagged as
trusted, BBJ items flagged as such, geography filtered to Boston-area only.
Window: **Sat Apr 26 → Fri May 2 morning.**

`news-summary` came back with **23 candidate items** matching your geography
filter. Of those, **5 cleared the "actually intersects with your portfolio
this week"** bar that your USER.md frames the brief around — the rest are
either out-of-scope (a State House budget item that doesn't touch Boston
directly), already known to you (the Codman Square modification you mentioned
earlier in the week), or the kind of low-signal council procedural that
doesn't deserve a bullet.

Drafting the trial brief in the shape we just landed on. One screen. Smart
staffer's voice. Will run `humanizer` on the framing line only — *not* on
the bullets — for the reason you've flagged before about humanizer turning
tight bullets into prose that no longer scans.

## Turn 7 — Andrew

Show me.

## Turn 8 — Assistant

---

> **Boston policy week — Fri May 1**
>
> Quiet-ish week, but two items worth your attention before Monday.
>
> - **City Council took up the storefront vacancy registration ordinance
>   Wed (committee).** Hearing only, no vote. The version on the table
>   would require commercial property owners with vacant ground-floor
>   space to register and pay an annual fee scaled to vacancy length.
>   *Intersects with:* Bowdoin–Geneva and your other corridor work — same
>   problem you've been thinking about, but the ordinance approach is a
>   different lever than what your office has been working on. Worth
>   knowing the council framing before it comes back up.
>
> - **BPDA staff floated a revised inclusionary development policy
>   memo internally Mon, leaked to *CommonWealth* Wed.** Headline change:
>   on-site affordability requirement bumped from 13% to 17% on projects
>   above a certain size threshold. *Intersects with:* anything in your
>   pipeline that's mid-filing — Codman Square major mod (Item 7 on
>   Thursday's BPDA Board) is already past the threshold under the old
>   number; not yet clear how the revised policy applies to filings
>   already in flight. *Status:* not yet public; *CommonWealth* has the
>   leaked memo but BPDA hasn't confirmed.
>
> - **MassDOT released the draft Fairmount Line corridor study, Thu.**
>   Most of it is rail-ops; the relevant piece for you is a recommendation
>   that pedestrian and bike infrastructure investments around the
>   Talbot Ave and Fairmount stations be coordinated with City of Boston
>   public realm planning. *Intersects with:* your Fairmount TOD grant
>   work — the recommendation is consistent with what you and Priya
>   discussed last Friday. No surprises.
>
> - **Mass legislature — H.2147 (small-business commercial lease
>   stabilization) reported favorably out of committee Tue.** Long road
>   to passage, but the bill is moving for the first time this session.
>   *Intersects with:* the small-business retention thread under your
>   Bowdoin–Geneva work, distantly. Worth tracking.
>
> - **Dorchester Reporter ran a profile of the new Codman Square NDC
>   board chair Wed.** Not a policy item per se, but the new chair is
>   the person Daniel works for, and the profile has a paragraph on the
>   NDC's posture toward City partnerships that's more candid than the
>   official line. Worth reading before the next Fairmount TOD touchpoint.
>
> **Watch list (next week):**
> - Storefront vacancy ordinance probably back at council in two weeks;
>   second hearing not yet scheduled.
> - The BPDA inclusionary memo will either be confirmed publicly or
>   walked back; either way, expect noise.

---

That's the trial. One screen, five items that actually intersect with your
portfolio this week, watch list with two items, no national, no
boosterish framing, BBJ items absent because nothing from them cleared
the relevance bar this week (so the "flag if from BBJ" rule didn't get
exercised yet — it's still in the default).

What's wrong with it? I want the format calibration grounded in your
reaction to the real thing, not in the abstract.

## Turn 9 — Andrew

Three things, and one of them is going to be a useful surprise to you.

One — drop "Quiet-ish week, but two items worth your attention before
Monday." That's the kind of cute framing-line that drifts into "Five
Things You Need to Know" territory if I let it. The framing line should
just be a date stamp and a one-sentence honest read, not a tease.

Two — I don't want *Dorchester Reporter*'s NDC board profile in the brief.
That's news, not policy. The line between "policy news" and "news from
people I work with" is one I want to keep clean — once you start mixing
them I'll get profiles every week and I'll stop trusting the brief to
have signal.

Three — and this is the surprise — I want a section you didn't propose.
**"What I should ask Imran or Michelle about Monday."** Sometimes one of
these items is not just intersecting with my portfolio in the abstract,
it's specifically a thing I should walk into the standup having flagged.
The BPDA inclusionary memo is exactly that this week — Michelle is the
one running point on the Codman filing and she may not have seen the
*CommonWealth* leak. One line, only when relevant, sometimes empty.

## Turn 10 — Assistant

All three folded in, and the third one is genuinely a better default than
what I had — "intersects with your portfolio in the abstract" and
"specifically worth raising with Imran or Michelle Monday" are different
signals and you're right that they should be different lanes. I would not
have proposed it.

Revised trial, with all three changes:

---

> **Boston policy week — Fri May 1**
>
> Two items this week move things in your portfolio; the rest is context.
>
> - **City Council took up the storefront vacancy registration ordinance
>   Wed (committee).** Hearing only, no vote. The version on the table
>   would require commercial property owners with vacant ground-floor
>   space to register and pay an annual fee scaled to vacancy length.
>   *Intersects with:* Bowdoin–Geneva and your other corridor work — the
>   ordinance approach is a different lever than what your office has
>   been working on.
>
> - **BPDA staff floated a revised inclusionary development policy memo
>   internally Mon, leaked to *CommonWealth* Wed.** Headline change:
>   on-site affordability requirement bumped from 13% to 17% above a
>   project-size threshold. *Status:* not yet public; *CommonWealth* has
>   the leaked memo but BPDA hasn't confirmed.
>
> - **MassDOT released the draft Fairmount Line corridor study, Thu.**
>   The relevant piece is a recommendation that pedestrian and bike
>   infrastructure around Talbot Ave and Fairmount stations be
>   coordinated with City of Boston public realm planning. *Intersects
>   with:* your Fairmount TOD grant work — consistent with what you and
>   Priya discussed last Friday.
>
> - **Mass legislature — H.2147 (small-business commercial lease
>   stabilization) reported favorably out of committee Tue.** Long road
>   to passage but moving for the first time this session.
>
> **Watch list (next week):**
> - Storefront vacancy ordinance probably back at council in two weeks;
>   second hearing not yet scheduled.
> - BPDA inclusionary memo: confirmed publicly or walked back; either
>   way, expect noise.
>
> **Worth flagging Monday:**
> - The BPDA inclusionary leak. Michelle is running point on the Codman
>   filing and may not have seen *CommonWealth* Wed; the threshold-vs-
>   in-flight question is the one to ask her about.

---

Cleaner. Four items now (Dorchester Reporter dropped — agreed it was a
profile, not policy). Framing line is a date and an honest one-sentence
read. New "Worth flagging Monday" lane has exactly one item this week
because exactly one item this week passes the bar — and that's the right
behavior, not a bug.

Anything else before I write this to memory as the default?

## Turn 11 — Andrew

Two more nits. "Worth flagging Monday" is the right header. Don't write
"Worth flagging Monday: (none)" on weeks when nothing clears the bar —
just omit the section entirely. An empty lane reads as the assistant
performing structure rather than reading the week. And under intersects-
with — for the H.2147 item, you didn't add an intersects line because
"distantly" was the honest read and I appreciate that you didn't
manufacture one to fill the slot. Make sure the saved default explicitly
permits items without an intersects line.

## Turn 12 — Assistant

Both folded into the default. Specifically:

- "Worth flagging Monday" is **omit-when-empty**, not present-with-(none).
  Captured in the saved default as "include section only on weeks where
  at least one item meets the bar; do not perform structure."
- *Intersects with* is now an **optional sub-line, not a required slot.**
  When the assistant cannot honestly say what an item intersects with in
  one line, the line is omitted; an item without an intersects line is
  not a malformed bullet, it's an honestly-classified bullet.

About to write to `memory`. Before I do — let me read the calibrated
default back to you in full, in the form it will be saved, so you can
spot anything that drifted from what you actually said vs. what I think
you said. This is the artifact that will run every Friday going forward,
so it's worth the extra minute now.

## Turn 13 — Andrew

Yes, read it back.

## Turn 14 — Assistant

Reading the saved default back, verbatim:

---

> **Andrew / Friday Boston policy news brief — saved default (set May 1, 2026)**
>
> **Trigger.** Summon-only. Brief is generated when Andrew asks for it.
> Do not auto-deliver, do not schedule a recurring email, do not push.
>
> **Window.** Saturday morning of the prior week through Friday morning
> of the requested week.
>
> **Geography filter.** Boston city, BPDA, Mass legislature when it
> touches Boston, MassDOT when it touches Boston. Cambridge or
> Somerville items only when they set a regional precedent likely to
> reach Boston. *Skip national policy news entirely*, even when it
> covers Boston — Andrew reads national elsewhere.
>
> **Source weighting.** Trusted: Globe metro desk, CommonWealth,
> Banker & Tradesman on real-estate items, Dorchester Reporter and
> Bay State Banner on neighborhood-level items. Boston Business
> Journal is allowable but skews promotional — flag any BBJ item
> in-line as `(BBJ — booster lean)`. Skip national outlets even when
> they cover Boston.
>
> **Format — one screen, no scrolling on phone.**
>
> 1. **Header.** `Boston policy week — Fri [date]`.
> 2. **Framing line.** One honest sentence reading the week. Not
>    a tease, not a "X things you need to know," not boosterish.
>    On a slow week, the line says so honestly.
> 3. **3–5 bulleted items**, each:
>    - one-line plain-language headline
>    - one line of what it is and why it matters
>    - *Intersects with: …* — **optional sub-line**, only when there
>      is a genuine intersection with something Andrew is actively
>      working on; omit rather than manufacture.
>    - *Status: …* — when an item is unconfirmed, leaked, or still
>      developing, say so.
> 4. **Watch list (next week)** — one or two items that haven't
>    broken yet but Andrew should expect.
> 5. **Worth flagging Monday** — items that are not just intersecting
>    in the abstract but specifically should be raised with Imran or
>    Michelle at Monday standup. **Omit the section entirely on weeks
>    where nothing clears the bar.** Do not present-with-(none).
>
> **Voice.** Smart staffer's plain-language read. Not neutral wire-copy.
> Not lightly-opinionated. No "exciting developments," no "transformative,"
> no "City Hall doubled down." Plain, short, honest.
>
> **Humanizer rule.** Apply only to the framing line. Do not apply to
> bullets — Andrew has flagged before that humanizer applied to tight
> bullets softens them into prose that no longer scans.
>
> **Negative defaults.**
>   - No national items.
>   - No "X Things You Need to Know" framing.
>   - No drafted talking points or attributable quotes.
>   - No profiles or personality pieces — policy news only. The line
>     between "policy" and "news from people Andrew works with" is
>     deliberately maintained.
>   - No scheduled push.
>
> **Calibration note.** This default was set in conversation on
> Fri May 1, 2026, working off a real week of Boston-area policy
> news (Trial brief covered: storefront vacancy ordinance hearing,
> BPDA inclusionary memo leak, MassDOT Fairmount study, H.2147 small-
> business commercial lease bill, with a "worth flagging Monday" lane
> on the BPDA leak for Michelle). Andrew explicitly added the "Worth
> flagging Monday" lane mid-session — the assistant did not propose it.

---

That's the saved version. Two specific things I want you to look at
before I commit it:

- **The negative default about profiles.** I wrote it as a hard rule
  ("no profiles or personality pieces — policy news only") rather than
  a soft preference. You dropped the *Dorchester Reporter* item this
  week with a clean reason, but on some future week there might be a
  profile worth knowing about (a new commissioner, a new BPDA director).
  Want it as a hard rule, or should I soften it to "default skip,
  surface only if the person is directly material to something Andrew
  is working on"?
- **The calibration note.** I left the trial-brief contents inline so
  if we're ever debugging why the default looks the way it does next
  year, the example that produced it is right there. If you'd rather
  the saved default be cleaner without the example, I can pull it out.

## Turn 15 — Andrew

On the profile rule — soften it. "Default skip, surface only if the
person is directly material to something I'm working on" is more honest
than a hard rule. On the calibration note — keep it inline. I'd rather
have the example available a year from now than a cleaner-looking memory
artifact.

## Turn 16 — Assistant

Both updates in. The relevant lines now read:

> **Negative default — profiles:** Default skip. Surface only if the
> person profiled is directly material to something Andrew is actively
> working on (e.g., a new BPDA director, a new chair of an organization
> Andrew has standing work with). Distinguish in the bullet line that
> the item is a profile, so Andrew can choose to drop it.

> **Calibration note:** Inline trial brief preserved for future
> reference. Do not strip on cleanups.

Writing to `memory` now.

`memory` write committed. Default is now active for any future Friday
session. Next time you open a chat and say "Friday brief," the format
above is what runs — no re-explaining, no calibration interview unless
you ask for one. If something about the format starts to drift over time
or stops fitting your week, the calibration session is short enough to
re-run.

One thing I want to confirm explicitly because it's the easiest piece to
get wrong silently: **summon-only is the active rule.** I will not push
a Friday brief into your inbox at 8 AM. The brief exists when you ask for
it. If you ever change your mind on this and decide you want a scheduled
push, that's a different setting and you'd have to flip it explicitly —
I won't quietly start auto-delivering after a few sessions.

## Turn 17 — Andrew

Confirmed. Don't auto-deliver, ever, unless I explicitly turn it on. One
question before we close out — I know we just calibrated this against one
week's news. What happens when next Friday's news week is shaped
completely differently — like a single huge story dominates and there
aren't four other items worth bulleting?

## Turn 18 — Assistant

Good question and the honest answer is the format I just saved is biased
toward "normal" weeks (3–5 items, mixed topics) and you'll want to know
how it behaves on the edges.

Two edge cases worth thinking about now so I'm not making a judgment call
in the moment when you summon a future brief:

- **Single-dominant-story week.** If one story is the week (a major
  ruling, a budget release, a public hearing on a hot item), I'd lead
  with that as the framing line ("This week was the [whatever] story
  and very little else"), give it one fuller bullet that does the work
  of two, and keep the brief shorter rather than padding to hit 3–5.
  Padding to format is exactly the failure mode we just designed
  against.
- **Genuinely empty week.** If the geography filter and relevance bar
  produce *fewer than three* items worth your attention, the honest
  brief is shorter than a screen, and the framing line says "Slow
  week — two items, neither big" or "Nothing this week that meets the
  bar." That's the brief. I'd rather hand you a four-line acknowledgment
  on a slow week than scrape three bullets to fill the format.

If you want, I'll add both of those as explicit edge-case rules in the
saved default so future sessions don't have to re-derive them. My read
is yes — they're the kind of thing that, if not written down, will
silently regress over time.

## Turn 19 — Andrew

Yes, add both. And add a third — if a single story is *not yet
confirmed* but is shaping the week (like the BPDA leak this week could
have been if it'd broken bigger), the framing line should say "this
week was probably about X, pending confirmation," not just commit to it
as the story. I want the brief to track honesty over neatness.

## Turn 20 — Assistant

Both edge-case rules and the third one in. The saved default now has
this section appended:

> **Edge-case behavior:**
>
> - **Single-dominant-story week.** Lead the framing line with the
>   story, give it one fuller bullet doing the work of two, keep the
>   brief shorter rather than padding to hit 3–5. Do not manufacture
>   bullets to fill the format.
> - **Empty or near-empty week.** Fewer than three items meeting the
>   relevance bar = a four- to six-line brief. Framing line says so
>   plainly ("Slow week — two items, neither big" or "Nothing this
>   week that meets the bar"). Do not scrape to fill.
> - **Probable-but-unconfirmed dominant story.** If a single
>   developing story is shaping the week but is not yet confirmed,
>   framing line reads "this week was probably about X, pending
>   confirmation" rather than committing to the story as fact. Track
>   honesty over neatness.

`memory` updated. The default is now what we just walked through, plus
the three edge-case rules.

Quick close-out so you have the state of play in one place:

- **Calibrated default for the Friday Boston policy news brief: saved
  to memory.** Picks up automatically next time you summon a brief; no
  re-calibration unless you ask.
- **Trigger:** summon-only. No auto-delivery, no scheduled push, no
  Friday-morning email. Confirmed twice on the record because it was
  the easiest rule to get wrong silently.
- **Today's trial brief:** the four-item Friday May 1 version above.
  Not saved as a sent artifact — it exists in this session's transcript
  if you want to refer back to it, but the *default* is the artifact
  that lives in memory. Tell me if you'd like me to also save the
  trial brief as a `.docx` for any reason.
- **One thing I deliberately did NOT save to memory:** any preference
  about *which specific stories* count as "intersecting with Andrew's
  portfolio." That's going to drift week-to-week as your portfolio
  drifts (Bowdoin–Geneva is hot now, in six months it might not be).
  The default captures the *rule* (intersects only when it intersects),
  not a frozen list of topics — so the brief stays useful as your work
  changes, instead of getting stale around what you cared about in
  May 2026.

## Turn 21 — Andrew

Don't save the trial as a docx — the point is the rule, not the example.
And good catch on the portfolio-drift thing. That would have been a
trap. Thanks.

---

## End of trajectory
**Total turns:** 21 (within the requested 20–22)
**Format:** First-person human dialogue throughout, alternating Andrew ↔
assistant.

**Tools exercised — all four:**
- `conversation` — used as the **calibration tool**, not as background
  chat. Five short structured questions (length, geography, sources,
  voice, delivery) that pin down the choices that genuinely change the
  artifact, then explicit "I'd rather over-ask than guess and have to
  un-set it later." The conversation pass is what makes this a
  preference-capture session rather than a guess-and-save.
- `news-summary` — used as the **live trial-run tool**. Pulled the actual
  Boston-area policy news for the week of Apr 26 → May 2, weighted to
  Andrew's trusted outlets, geography-filtered to Boston-area only.
  23 candidate items came back, 5 cleared the relevance bar, the brief
  was built off real items. The calibration is grounded in Andrew's
  reaction to the real thing, not in hypotheticals.
- `humanizer` — used as a **scalpel** in the trial brief (framing line
  only, never bullets), and the *rule* about that scalpel application
  was captured in the saved default so the same restraint applies on
  every future Friday. Andrew's prior observation about humanizer
  softening tight bullets into unscanable prose is preserved as a
  durable rule, not a one-time instruction.
- `memory` — the **destination tool**. The calibrated default was
  written to memory in full, *read back verbatim* before the write so
  Andrew could spot drift between what he said and what was being
  saved, and explicitly tagged with a calibration note (date, trial
  brief contents inline, novel-lane provenance) so the artifact is
  auditable a year from now.

**Behaviors demonstrated:**
- **Live trial run before saving the default.** The format is
  calibrated against a real week's worth of news, not against a
  hypothetical week. Andrew's reactions to the real thing surface
  preferences he wouldn't have articulated in the abstract — including
  the "Worth flagging Monday" lane he asks for that the assistant did
  not propose, and the optional-intersects-line rule that prevents
  manufactured intersections.
- **Reads the default back verbatim before committing.** Treats the
  memory write as a durable artifact that's easier to get right now
  than to debug later. Surfaces two specific lines (profile rule;
  calibration-note inclusion) for explicit Andrew sign-off rather
  than committing them silently.
- **Pushes back on auto-delivery** with substantive reasoning (inbox
  fatigue, three-week half-life on auto-newsletters), then captures
  "summon-only" as a hard rule in the saved default, and confirms it
  twice on the record because it's the easiest rule to silently
  regress.
- **Edge-case rules elicited proactively** at Andrew's prompt about
  what happens on a single-dominant-story or empty week. Three
  edge-case behaviors written into the default (single-dominant,
  empty, probable-but-unconfirmed), all biased toward honesty over
  neat formatting.
- **Refuses to freeze portfolio specifics into the default.** Saved
  the *rule* ("intersects with Andrew's portfolio") rather than a
  list of currently-hot topics, so the brief stays useful as the
  portfolio drifts over time. Surfaced this distinction proactively
  at the close.
- **Boston-anchored throughout.** All location and source references
  are explicitly inside the persona's city (Boston city government,
  BPDA, MassDOT-when-it-touches-Boston, named Boston outlets, named
  Boston neighborhoods).
