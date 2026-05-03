# Trajectory: Pick Up the Ongoing Civic Fellowship Outreach Plan and Prep the Next Moves

**User:** Andrew (Deputy Director of Community Development, Boston city government)
**Tools available:** `memory`, `conversation`, `subagent`, `edit`, `gmail`,
`word-docx`, `humanizer`
**Goal:** Resume previously-extensive multi-session work on the Boston
Neighborhoods Civic Fellowship. Use memory to pull what's settled (without
making Andrew re-explain it). Detect that the framing has quietly drifted
into vague community-language since the last working session. Re-ground the
framing through a short calibration conversation, supported by one
well-scoped subagent pull of comparable small-city fellowship language as
real comparators. Then produce two outreach drafts in two registers — one
to a partner organization, one to a prospective fellow — and write the
re-grounded framing back to memory so this conversation doesn't have to
repeat in the next session.
**Turn count:** 21 (alternating user / assistant; first-person human dialogue only)

---

## Turn 1 — Andrew

Can we pick back up on that civic fellowship thing? I know we've already
done a ton on it and I really don't want to start from scratch again.

## Turn 2 — Assistant

Pulling `memory` first so we're picking up, not restarting.

`memory` recall, in one breath so you can confirm I'm looking at the right
thread: **Boston Neighborhoods Civic Fellowship** — small, year-long
program, **8 fellows**, modest stipend (we settled on **$6,000 over the
year** per fellow plus a small project budget), six neighborhoods in
scope (Bowdoin–Geneva, East Boston, Mattapan, Hyde Park, Allston, and
the West End). Fellow profile: Boston residents, 18+, with a stated
interest in how the City does neighborhood-level work, no prior
professional credential required (you and Samuel were specific that this
was a non-credential program — the whole point was to reach people
*outside* the existing civic-engagement crowd). Two confirmed partner
organizations: **Codman Square Neighborhood Development Corporation**
and **East Boston Main Streets**. A third — Boston Tenant Coalition —
was in conversation but parked because Yolanda Reyes was bandwidth-
constrained on the rent stabilization comment period (separate thread).

**On the operational side:** Samuel holds program design; Darian holds
outreach and candidate communications; you hold the framing and the
partnerships. **Settled timeline:** soft launch Sep 2026, applications
open Jul–Aug, partner-org outreach to wrap by end of June.

**Previously rejected phrasings** captured from prior sessions: "lift
up resident voices," "co-create solutions with the community," "build
community capacity," "amplify lived experience" — you specifically
flagged each of these and the *reasons* are in memory too (they sound
like the program isn't real yet).

That's the state. Three quick questions before I propose a next step:

1. **What prompted you to come back to this today?** A deadline
   approaching, a conversation you had, or just bandwidth opening up?
   The right next step depends on which.
2. **Anything moved since we last worked on it?** Off-system updates,
   conversations with Samuel or Darian, anything from the partner
   organizations.
3. **What's actually blocking the next outreach going out?** My read
   from where we left off is that the next-step note was supposed to
   go to one or two more partner organizations to lock in by end of
   June, but I want to confirm before I draft.

## Turn 3 — Andrew

Two things prompted it. One — Darian needs to start sending outreach to
prospective fellows mid-June and she can't do that until the program
description is locked, and right now it isn't. Two — I had coffee with
Samuel yesterday and he said something that's been bugging me since.
He's been reviewing the latest draft of the program description and the
partner one-pager, and he said the language has slowly drifted back into
exactly the territory we explicitly killed two sessions ago. "Activate
community wisdom." "Civic capacity-building cohort." His read is that
because we've been working on this for months and the document keeps
getting iterated on, the phrases creep back in without anyone noticing.
He's right. So before *any* outreach goes out — to partners, to
prospective fellows, anywhere — the framing has to get re-grounded.
That's what I want to do today.

## Turn 4 — Assistant

That's the right diagnosis and Samuel's read of *why* it happens is
also right — iterative document drift toward the genre's gravity well
is exactly how programs end up sounding like the thing you spent two
sessions killing. Glad we caught it before it went out the door.

Re-grounding the framing first, then everything else downstream of it
gets cleaner automatically. Plan, three steps:

1. **Short `conversation` calibration pass** — five questions, not
   twenty, structured to re-pin the language against what the
   *fellow actually does*. The phrases drift back in because nobody
   re-asks "what is a fellow concretely doing in week 3 of this
   program;" once you can answer that, the boilerplate has nowhere
   to land.
2. **One `subagent` pull** for real comparators — how comparable
   small-city civic fellowships in other US cities (Providence,
   Pittsburgh, Buffalo, Tulsa, etc.) describe their fellows'
   actual work. The reason this is worth doing as a separate pull
   is that the genre has *exemplars* (programs that describe
   concrete activity) and *anti-exemplars* (programs that sound
   exactly like our drift), and seeing both side-by-side makes the
   anti-pattern obvious in a way that's easier to point at than to
   describe abstractly. **One pull, single output, no candidate-
   fellow research** — that's a separate thing Darian does
   relationally, not via tool scrape.
3. **Re-write the framing block** with the calibration conversation
   and the comparators in front of us, then propagate it forward to
   the program description, the partner one-pager, and the
   prospective-fellow outreach Darian needs to start.

Then we draft outreach. Sound right, or should we sequence it
differently?

## Turn 5 — Andrew

That's the right sequence. Run the conversation pass.

## Turn 6 — Assistant

Five questions. Quick answers are fine — I'm calibrating language, not
rebuilding the program.

1. **Concretely, what does a fellow do in week 3?** Not the program's
   purpose — the activity. If you had to point at a fellow on a
   random Wednesday afternoon in week 3 and say "she is doing X
   right now," what is X?
2. **Concretely, what does a fellow produce by month 6?** A document?
   A relationship? A project? A piece of work she could put on a
   resume?
3. **What is the City actually offering a fellow that they cannot
   get without this program?** Stipend aside — what's the access,
   the relationship, the experience that makes this program a
   real thing?
4. **What is a fellow *not* expected to be?** Where do you and
   Samuel want to draw the line — explicitly — between a fellow
   and other things people might assume the role is (an intern,
   an advocate, a peer-researcher, an unpaid consultant)?
5. **Who is the prospective fellow most likely to be confused
   with this program by a similar-sounding program**, and what's
   the differentiator you'd want to lead with against that
   comparator?

## Turn 7 — Andrew

1. Week 3 — she's sitting in on a real working meeting in her
   neighborhood. Not a community meeting that was set up for the
   fellows — an actual operational meeting that was going to happen
   anyway. Could be a Main Streets board meeting in East Boston, a
   permitting working group in Bowdoin–Geneva, a planning conversation
   with a CDC staff person in Mattapan. She's there to see how the
   thing actually runs, with the people whose job it is to run it.
2. Month 6 — she's produced a short, plain-language analysis of one
   specific operational thing she watched up close. Not a community
   needs assessment, not a recommendations memo. Something more like
   "I sat in on the East Boston Main Streets board's permitting
   discussions for four months and here is what I observed about how
   small businesses navigate the City's signage process." Concrete,
   specific, useful to actual people.
3. The City is offering her something she structurally cannot get
   otherwise — *seated access to operational rooms in her own
   neighborhood for a year*. Not a town hall, not a panel, not a
   listening session. The actual rooms. That's the thing.
4. She is not an intern (we are not training her to do our jobs), not
   an advocate (we are not asking her to lobby for or against
   anything), not a peer-researcher (this is observation in context,
   not academic methodology), and not an unpaid consultant (the
   stipend is a real stipend, and she is not being asked to deliver
   work product for the City). Drawing each of those lines explicitly.
5. Most likely confusion: with one of the universities' civic
   leadership programs that recruits the same demographic. Those are
   *training programs* — fellows go through a curriculum. Ours isn't.
   The differentiator is that ours puts a fellow into an operational
   room, not a classroom.

## Turn 8 — Assistant

That's an enormous amount of clarity in five answers and it makes the
re-grounding work itself almost mechanical. Reading back what we now
have to anchor against — the framing block now has to honor all five:

- Week 3 = sitting in operational rooms in her neighborhood.
- Month 6 = a short plain-language analysis of one specific
  operational thing observed.
- City's offer = seated access to operational rooms for a year.
- Not = intern, advocate, peer-researcher, unpaid consultant.
- Differentiator vs. university civic leadership programs =
  operational room, not classroom.

Spinning the `subagent` up now to grab comparators while you think
about whether you want to refine any of those answers.

**Subagent dispatched.** Single task, single output:

> Survey small-city civic fellowship programs in other US cities
> (suggested starting set: Providence, Pittsburgh, Buffalo, Tulsa,
> Louisville, Birmingham, Cincinnati — add others if you find them
> as you go). For each, extract two things: (a) one or two sentences
> from how the program publicly describes what a fellow concretely
> does, and (b) the program's framing-language register (concrete-
> activity vs. capacity-building-genre).
>
> Surface as: 4–6 *exemplars* (programs that describe concrete
> activity Andrew would respect) + 4–6 *anti-exemplars* (programs
> that sound exactly like the drift Andrew is trying to fix), with
> the verbatim public language in each case so we're working from
> evidence, not paraphrase. **Do not include any individual fellows
> by name.** This is program-language research, not person research.
>
> Due back in this session.

I'll surface what comes back when it lands.

## Turn 9 — Andrew

Good. While that runs — your phrasing back at me of the five answers
is mostly right, but tighten one: I would not say "seated access to
operational rooms" in any document. That phrase reads to me like
"corridors of power" coded language and I don't love how it sounds.
Functionally it's right. As language it's wrong. Find a better way to
say it.

## Turn 10 — Assistant

Fair — you're right that "seated access to operational rooms" is
exactly the kind of phrase that *sounds* concrete because it has nouns
in it but actually carries an institutional self-importance you don't
want anywhere near the program. Three alternatives, increasingly
plain:

(a) "Sitting in on the working meetings where neighborhood-level City
    decisions actually get made."
(b) "Spending the year in the operational meetings of a Boston
    neighborhood's civic and economic life — the ones that would
    happen whether the fellow was there or not."
(c) "A year of sitting in the room where the work happens, in your
    neighborhood, with the people whose job it is to do it."

My read is (b) for the program description (one full sentence, no
glamorization, lands the "would happen anyway" point that
distinguishes us from a program that stages meetings for fellows),
and (c) for the prospective-fellow outreach (warmer, more direct, lets
the fellow picture herself in it). Not (a) — "where neighborhood-level
City decisions get made" still has a residue of the importance-coded
register.

Pick one or one of each, and `subagent` is back so I'll surface its
output next.

## Turn 11 — Andrew

(b) for the program description, (c) for the prospective-fellow
outreach. Show me the subagent output.

## Turn 12 — Assistant

Subagent back. Surfaced **5 exemplars and 5 anti-exemplars** from 11
small-city civic fellowships scanned. Brief read, with verbatim public
language so the contrast is clear:

**Exemplars (programs that describe concrete activity):**

- *Providence* — "Fellows are paired with a city department for the
  year and attend the department's regular operational meetings and
  service-delivery activities." (Concrete: paired-with, attend
  regular meetings.)
- *Pittsburgh* — "Each fellow shadows one of three working groups
  and produces a short observational report by program end." (Has
  a deliverable shape; uses the word "shadows.")
- *Tulsa* — "Fellows commit to one neighborhood and one ongoing
  initiative within it for the program year." (Specific; not
  "engages with community.")
- *Louisville* — "By month 8 each fellow files a 4–6 page memo
  describing the operational dynamics of the initiative they
  followed." (Names the artifact; names the length; names the
  shape.)
- *Cincinnati* — "Fellows are not staff and are not making
  recommendations on behalf of the City." (Explicit boundary —
  what the fellow is not. Same move you made in answer #4.)

**Anti-exemplars (sound exactly like our drift):**

- One program — "Activates community wisdom by elevating
  resident-led pathways to civic transformation." (Exactly the
  register Samuel flagged. Could be any program in any city.)
- Another — "A capacity-building cohort for next-generation
  civic leaders." (Reads as training; doesn't actually say what
  the fellow does.)
- Another — "Co-creating equitable futures alongside our
  community partners." (Three flagged-by-you phrases in one
  sentence.)
- Another — "Empowering residents to be the change-makers their
  neighborhoods deserve." (Aspirational; the fellow's actual
  activity is invisible.)
- Another — "A platform for marginalized voices to drive
  systems-level change." (Same problem; the fellow does not
  appear in this sentence.)

Two patterns worth noticing:

- The exemplar programs almost always **name an artifact**
  (Pittsburgh: report; Louisville: 4–6 page memo) and **name
  what the fellow is not** (Cincinnati). You did both naturally
  in your answers — that should be in the framing block, not
  just implied.
- The anti-exemplars don't have *the fellow* in the sentence.
  The grammatical subject of every anti-exemplar above is an
  abstraction (community wisdom, capacity, change-making,
  voices) — not a person doing a thing. If our framing has the
  fellow as the subject of the sentence, the genre's gravity
  has nowhere to pull.

Want me to draft the re-grounded framing block now using all of
that, before we move to outreach?

## Turn 13 — Andrew

Yes draft it. And the "fellow as grammatical subject" rule is going
into memory — that's the kind of small mechanical principle that
prevents drift better than a hundred style notes.

## Turn 14 — Assistant

Captured for memory at the close. Re-grounded framing block, drafted
to honor the five clarity points + the artifact-naming pattern +
fellow-as-subject + the not-list + your phrasing choice (b) for the
program description register:

---

> **Boston Neighborhoods Civic Fellowship — what it is**
>
> A fellow spends the year in the operational meetings of a Boston
> neighborhood's civic and economic life — the ones that would happen
> whether the fellow was there or not. A Main Streets board meeting in
> East Boston. A permitting working group in Bowdoin–Geneva. A
> planning conversation between a CDC and a small-business operator
> in Mattapan. The fellow is in the room.
>
> By month 6, the fellow produces a short, plain-language analysis
> of one specific operational thing observed up close — typically a
> 4–6 page document. The program's full year produces eight of those
> documents, one per fellow, drawn from six neighborhoods.
>
> **A fellow is not** an intern (we are not training fellows to do
> City staff jobs), an advocate (we are not asking fellows to lobby
> for or against any position), a peer-researcher (this is
> observation in context, not academic methodology), or an unpaid
> consultant (the stipend is a real stipend, and the fellow is not
> being asked to deliver work product for the City).
>
> The program runs from September through the following August,
> serves eight fellows across six Boston neighborhoods, and pays
> a $6,000 stipend per fellow over the year plus a small project
> budget.

---

Two things I'd flag about the draft:

- Every sentence has a fellow (or *the fellow*) as the grammatical
  subject of the actual activity verb. No "wisdom is activated."
  No "voices are amplified." A person does a thing.
- The "is not" paragraph is doing real work — it's not just a
  legalism, it's the place where prospective fellows from outside
  the existing civic-engagement crowd will recognize whether this
  is or isn't for them. The most reliable way to recruit the
  people you and Samuel said you wanted to reach is to be
  explicit about what the role *isn't*.

Greenlight on the framing block, or one more pass before we move to
outreach?

## Turn 15 — Andrew

Greenlight, that's the version. Now drafts. I want one for partner
organizations — Codman Square NDC and East Boston Main Streets are the
two confirmed, the language we use to them needs to fit a peer
institution we already have a relationship with. And one for
prospective fellows — that's the one Darian needs to start sending
mid-June, so the warmer (c) register. Two drafts. Don't pad them.

## Turn 16 — Assistant

Two drafts, two registers. No padding.

**Draft 1 — Partner organization (institutional but warm,
peer-to-peer).** This goes to Daniel at Codman Square NDC and to
the equivalent at East Boston Main Streets. Pre-`humanizer`, showing
you raw first.

---

> **Subject:** Civic fellowship — confirming the partner-side ask
>
> Daniel —
>
> Following up on what we landed on in our March conversations, since
> we're getting close to the soft launch date.
>
> The Boston Neighborhoods Civic Fellowship runs Sep 2026 – Aug 2027.
> Eight fellows, six neighborhoods. Codman Square NDC is one of the
> two confirmed neighborhood partners, with one or two fellows placed
> in your operational rhythm for the year.
>
> What we are asking of NDC concretely: one staff-side point of
> contact for the year (not a heavy lift — quarterly check-ins, plus
> the practical question of which of NDC's regular working meetings
> the fellow can sit in on); a willingness for the fellow to be in
> the room as an observer, not a contributor, on most of those
> meetings; and one half-hour conversation with the fellow at month
> 1 to set expectations.
>
> What we are *not* asking: any work product from NDC, any new
> programming designed for the fellows, or any compensation. The
> stipend is on us.
>
> If anything in that scope reads differently from how we discussed
> it, flag it now rather than later. Otherwise, Darian on my team
> will be in touch in the next two weeks with the practical
> coordination piece (which staff person, which meetings, scheduling
> the month-1 conversation).
>
> Thanks,
> Andrew

---

**Draft 2 — Prospective fellow (warmer, less institutional, no false
intimacy).** This is the template Darian will adapt per recipient
once we have candidate names. Pre-`humanizer`.

---

> **Subject:** A small civic fellowship in your neighborhood — would
> this be of interest?
>
> Hi —
>
> I'm reaching out from the City of Boston about a small program we
> are launching this fall, the Boston Neighborhoods Civic Fellowship.
> Your name came up as someone we'd like to invite to apply.
>
> The shape of the program: a year of sitting in the room where the
> work happens, in your neighborhood, with the people whose job it
> is to do it. Working meetings, not town halls. Operational, not
> ceremonial. By month 6, you'd write a short — 4–6 page — analysis
> of one specific thing you observed up close.
>
> What you would *not* be: an intern, an advocate, a researcher, or
> an unpaid consultant. We are not asking for work product. The
> stipend is real ($6,000 over the year, plus a small project
> budget) and reflects the time the program asks of you.
>
> Eight fellows, six Boston neighborhoods, September 2026 through
> August 2027. Applications open in July; we're reaching out
> earlier to a small number of people to make sure the invitation
> lands before the application window opens.
>
> If this sounds interesting and you want to know more, I'd be
> glad to set up a 20-minute conversation with one of my colleagues
> on the program team. If it's not for you, no need to respond — and
> no hard feelings. I know unsolicited outreach about civic programs
> goes in a lot of inboxes that don't need it.
>
> Thanks for your time,
> Darian
> [on behalf of Andrew, Deputy Director of Community Development,
> City of Boston]

---

`humanizer` next on the cover lines and the human-voice
passages of each — *not* on the "what we are asking / what we are not
asking" sections, *not* on the program-shape framing, because those
are the structure-doing-the-work parts and humanizer would soften
them in exactly the wrong direction. Two short passages per draft.
Show you the before/after?

## Turn 17 — Andrew

Show me the before/after, but only on what you actually want to
change. If a passage doesn't need it, don't run it just for show.

## Turn 18 — Assistant

Right — only running it where it earns its keep. Three passages
total across the two drafts, not four.

**Draft 1 (partner) — "If anything in that scope reads
differently…" sentence.**
- *Before:* "If anything in that scope reads differently from how
  we discussed it, flag it now rather than later."
- *After:* "If any of that doesn't match what we discussed, tell me
  now — easier to fix this week than next."
- Notes: rewrite is closer to your actual voice with Daniel; the
  before reads slightly more institutional than the relationship
  warrants. I'd accept.

**Draft 2 (prospective fellow) — opening line.**
- *Before:* "I'm reaching out from the City of Boston about a small
  program we are launching this fall, the Boston Neighborhoods
  Civic Fellowship."
- *After:* "I'm writing from the City of Boston about a small
  program we're launching this fall — the Boston Neighborhoods
  Civic Fellowship."
- Notes: tiny edit, but "I'm writing" reads warmer than "I'm
  reaching out" (which has acquired a slightly transactional
  flavor in unsolicited outreach over the last few years).

**Draft 2 — "If it's not for you, no need to respond" passage.**
- *Before:* "If it's not for you, no need to respond — and no
  hard feelings. I know unsolicited outreach about civic
  programs goes in a lot of inboxes that don't need it."
- *After:* "If it's not for you, no need to write back. I know
  this kind of unsolicited outreach lands in a lot of inboxes
  that didn't ask for it."
- Notes: "no hard feelings" was reading slightly chummy for a
  cold outreach to someone Darian doesn't yet know. The rewrite
  preserves the no-pressure intent without the false-intimacy
  flavor.

I did **not** run humanizer on the "what you would not be"
paragraph, the program-shape paragraph, or the partner draft's
"what we are asking / not asking" block — those are the
structure-bearing parts where the precision is the value.

Take all three, take some, take none?

## Turn 19 — Andrew

Take all three. Save both as drafts on my work account — partner one
to me as the sender, prospective-fellow one as a draft on Darian's
account so she can adapt it per candidate when she's ready. Don't
send either. And then write everything to memory so the next session
picks up clean.

## Turn 20 — Assistant

Both saved. Status:

- **Partner draft** — saved as a Gmail draft on your work account,
  To: Daniel (Codman Square NDC), no Cc, subject line as drafted.
  Sitting in your Drafts. *Not sent.* I'll save a parallel draft for
  the East Boston Main Streets contact when you have the right
  person's email handy — placeholder for now.
- **Prospective-fellow draft** — saved on Darian's work account as
  a Drafts-folder template, with *[recipient name]* as the
  greeting placeholder so she can adapt per candidate. Subject line
  as drafted. *Not sent, by design — Darian will send when she has
  the candidate names and is ready to adapt the body.*
- **Program description** with the re-grounded framing block —
  saved as a `.docx` via `word-docx` to the team's Drive
  fellowship folder, replacing the prior version (the prior version
  is preserved in Drive's version history; no parallel
  pre/post-audit files cluttering the folder).

**`memory` writes — three, deliberately separate so they're each
recoverable:**

1. **Re-grounded framing block** (the four-paragraph "what it is"
   text), saved as the canonical fellowship description. Future
   sessions pull this when generating any fellowship-related
   document.

2. **Five-question calibration framework** (the questions I asked
   on turn 6), saved as a re-callable framework so when a future
   document or outreach drift happens, we can re-run the same five
   questions in 10 minutes rather than rediscover them.

3. **Two new durable rules** added to the fellowship-thread
   memory:
   > a. **Fellow-as-grammatical-subject rule.** In any
   > fellowship-related sentence describing what the fellow does,
   > the grammatical subject is the fellow (or "the fellow"), not
   > an abstraction (community wisdom, capacity, voices, change).
   > Drift is detected by reading any draft and asking who the
   > subject of each verb is.
   > b. **Artifact-and-not-list rule.** Any public-facing
   > fellowship description must (i) name the concrete artifact
   > the fellow produces by month 6, and (ii) include an explicit
   > "what a fellow is not" block. Both patterns drawn from
   > exemplar programs surfaced this session (Pittsburgh,
   > Louisville, Cincinnati).

That's the session. Quick recap so you have the state of play in
one place:

- **Framing re-grounded** through a five-question calibration
  pass plus an exemplar/anti-exemplar comparators pull. Samuel's
  diagnosis of drift was correct; the drift was caught and reversed
  before any outreach went out.
- **Two outreach drafts** in two registers, three small
  humanizer-edited passages, both saved as drafts (partner on your
  account, prospective-fellow template on Darian's), neither sent.
- **Program description** updated in place in the Drive fellowship
  folder.
- **Memory updated** — framing block, calibration framework, two
  new durable rules — separately enough that each is independently
  recoverable.

**What I deliberately did NOT do:**
- I did not spawn a subagent to research candidate fellows. That's
  Darian's relational work, not a tool scrape, and the privacy
  posture for a public-facing City program matters.
- I did not draft a public announcement or press release. Not asked
  for, and probably not the right next artifact anyway — the
  partner-and-fellow outreach lands first, the public announcement
  comes after.
- I did not send anything. Both drafts are sitting in their
  respective accounts for your and Darian's review.

## Turn 21 — Andrew

That's exactly what I needed. The fellow-as-subject rule is the
one I'll be quoting back at Samuel for the next year. Thanks.

---

## End of trajectory
**Total turns:** 21 (within the requested 20–22)
**Format:** First-person human dialogue throughout, alternating
Andrew ↔ assistant.

**Tools exercised — all seven:**
- `memory` — pulled the prior multi-session fellowship thread on
  turn 2 (program scope, fellow profile, partner orgs, settled
  decisions, previously-rejected phrasings with reasons) without
  reconstruction. At close: three deliberate separate writes —
  re-grounded framing block, five-question calibration framework,
  two new durable rules — so each is independently recoverable in
  future sessions.
- `conversation` — used as a calibration tool, not background
  chat. Five short structured questions structured to re-pin the
  language against what the fellow concretely does, deliberately
  designed so the genre's boilerplate has nowhere to land in the
  answers.
- `subagent` — used once with a tightly scoped task (small-city
  civic fellowship language survey: 4–6 exemplars, 4–6
  anti-exemplars, verbatim public language). Single output. The
  USER.md privacy line was honored (no candidate-fellow research)
  and re-stated in the dispatch instructions.
- `edit` — small surgical pass on the framing block alternatives
  (three phrasings produced; one chosen for the program
  description, one for the fellow outreach, one rejected with
  reason).
- `gmail` — two drafts saved on appropriate work accounts (partner
  draft on Andrew's; prospective-fellow template on Darian's, with
  greeting placeholder), neither sent. Different audiences =
  different accounts = different drafts; explicitly preserved.
- `word-docx` — program description with re-grounded framing
  saved to the fellowship Drive folder, replacing in place per the
  document-as-source-of-truth pattern.
- `humanizer` — applied to exactly three short passages across the
  two drafts (one in the partner draft, two in the prospective-
  fellow draft); explicitly *not* applied to the "what we are
  asking / what we are not" block, the "what a fellow is not"
  block, or the program-shape framing — those are structure-
  bearing content where humanizer's smoothing would erode the
  precision doing the work. Before/after shown for each, with
  individual veto.

**Behaviors demonstrated:**
- **Resumes prior multi-session work without reconstruction.**
  Settled decisions are treated as settled.
- **Detects framing drift early and addresses it before outreach.**
  Doesn't paper over Samuel's diagnosis; doesn't send drafts that
  carry the drift.
- **Calibration through structured short conversation**, not
  free-form chat. The five questions are designed to be the right
  five — each one targets a place where the genre's boilerplate
  would otherwise creep in.
- **Real comparators, not abstract advice.** Subagent surfaces
  verbatim public language from named real programs, exemplars
  alongside anti-exemplars; the comparator pull is what lets the
  re-grounding be evidence-based instead of taste-based.
- **Refuses to run a subagent on candidate fellows** for privacy
  reasons; names this explicitly when the subagent is dispatched
  rather than waiting to be asked.
- **Surfaces small-mechanical drift rules** (fellow-as-grammatical-
  subject; artifact-and-not-list) and writes them to memory as
  durable principles, because mechanical rules prevent drift
  better than style notes.
- **Two registers from one source, in one session.** Partner
  draft is institutional-peer; prospective-fellow draft is
  warmer-but-not-falsely-intimate. Same underlying program
  description; meaningfully different drafts.
- **Pushes back on humanizer-for-show.** Only humanizes passages
  that earn it; explicitly does not humanize structure-bearing
  passages.
- **Two drafts saved to two different accounts** matching the
  team's actual ownership of partner vs. fellow communications.
- **Closes with explicit "what I deliberately did NOT do"**
  including the candidate-research subagent, a public
  announcement / press release, and any actual sends.
- **Boston-anchored throughout** (Bowdoin–Geneva, East Boston,
  Mattapan, Hyde Park, Allston, West End, Codman Square NDC,
  East Boston Main Streets, Boston Tenant Coalition, City of
  Boston) and `USER.md` location anchored.
