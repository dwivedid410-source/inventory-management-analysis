# Trajectory: Coordinate a Multi-Step Testimony Prep Workflow for Next Week's Public Meeting

**User:** Andrew (Deputy Director of Community Development, Boston city government)
**Tools available:** `cron`, `subagent`
**Goal:** Set up a deliberately lightweight prep workflow for a Boston City Council
hearing eight days out — break the prep into discrete pieces, use `cron` for two
useful reminders (not five), use `subagent` for one well-scoped delegated piece
(not three), and explicitly leave the things that have to live in Andrew's voice
on Andrew's plate.
**Turn count:** 21 (alternating user / assistant; first-person human dialogue only)

---

## Turn 1 — Andrew

I have a public meeting next week and I can already feel myself doing the thing
where I keep all the prep in my head until it's suddenly a problem. Can you help
me set up a simple workflow with reminders and maybe split the work up so I don't
drop something dumb?

## Turn 2 — Assistant

Yes — and I'll keep "simple" honest. Two questions before I touch anything,
because they completely change what the workflow looks like:

1. **What kind of public meeting** — City Council hearing, commission meeting,
   community workshop, something else? "Public meeting" is doing a lot of work
   in that sentence and the prep shape is different for each. A Council hearing
   has written-submission deadlines and a strict speaker order; a community
   workshop doesn't. I want to make sure I'm scaffolding against the right
   thing.
2. **What day next week, and what's your role in the room** — testifying,
   presenting, on a panel, just attending and prepared to answer? Same point —
   a 3-minute oral testimony is a different prep than a 20-minute deck.

Once I have those two I can lay out a real deadline structure, not just "the
meeting." A lot of what gets dropped on these isn't the meeting itself — it's
the sub-deadlines that fire days earlier and don't show up on your calendar.

## Turn 3 — Andrew

City Council hearing. Committee on Housing & Community Development. **Wednesday
May 13, 2 PM.** I'm testifying on behalf of the department on the FY27 housing
pipeline — three minutes of oral remarks, then committee questions. Probably 20
to 30 minutes of questions, knowing this committee. I'll be the only person from
my office in the room. My director has signed off on the broad position but I
write my own remarks and answer my own questions.

## Turn 4 — Assistant

Okay — that changes the picture. The hearing is May 13 but the **real first
deadline isn't May 13.** Council clerk's office requires written testimony
submitted by **5 PM the Monday before the hearing** for it to be entered into
the official record. That's **Mon May 11, 5 PM**. If you only think about "the
meeting on Wednesday," you'll miss the Monday cutoff and your written remarks
won't be in the record — which on a housing pipeline hearing actually matters,
because committee staff read the written submission *before* the hearing and
their questions are partly shaped by it.

So the real deadline structure for you is:

- **Mon May 11, 5 PM** — written testimony submitted to the clerk. Hard deadline.
- **Tue May 12** — internal pre-brief with your director (you said he's signed
  off on position; this is the read-through-my-actual-remarks check). Soft, but
  he'll want it.
- **Wed May 13, 2 PM** — the hearing itself. Three minutes of oral remarks,
  20–30 minutes of Q&A.

Working backwards from Mon May 11, "do nothing until the day before" gives you
roughly **Sunday afternoon May 10** to write a clean three-minute oral version,
a written submission (typically longer — three to five pages with exhibits),
and brief your director. That's a tight Sunday. So the actual prep we're
scaffolding starts this week, not next.

Before I propose a workflow, two more questions because I don't want to
over-engineer:

- Do you want me to spin up a `subagent` to pull what comparable witnesses got
  asked at the **last two or three FY-housing-pipeline hearings** in front of
  this committee, so you walk in knowing the question shape? That's a
  well-scoped delegated job and it would meaningfully reduce Q&A surprise.
- For reminders, I'm assuming you want **two cron pings**, not five — one a few
  days out to start the written draft, one the morning of the clerk deadline.
  Tell me if I'm wrong about that.

## Turn 5 — Andrew

Yes on the subagent — that's exactly the kind of thing I would not do myself
and would regret not having. Two cron pings is right, do not give me five. And
nice catch on the Monday clerk deadline, I genuinely was going to miss that.
Walk me through what the workflow looks like end-to-end before you start
setting anything up.

## Turn 6 — Assistant

Good. Here's the end-to-end before we touch `cron` or `subagent`. I'm
deliberately keeping it on one screen — if it doesn't fit on one screen it's
already too much.

**Workflow — May 13 hearing prep (8 days out)**

| When | What | Owner |
|---|---|---|
| Today (Sun May 3) | Spin up subagent: pull last 2–3 FY-housing-pipeline hearing transcripts from Council clerk archive; surface (a) what committee members asked, (b) which members asked the sharp ones | subagent (delegated) |
| Tue May 5 | You skim the subagent's report (~10 min). Note the 3–4 likeliest question themes you want to be ready for. | You |
| Thu May 7 8 AM | **cron ping #1**: "Start the written submission draft this weekend. Pipeline data lives in [folder]." | cron |
| Sat May 9–Sun May 10 | Write the three-minute oral remarks (in your voice — your job, not delegated) and the 3–5 page written submission. | You |
| Sun May 10 evening | Self-check the written submission against the question themes the subagent surfaced. | You |
| Mon May 11 8 AM | **cron ping #2**: "Written testimony due to Council clerk by 5 PM today. Director pre-brief is tomorrow — confirm time." | cron |
| Mon May 11 ≤ 5 PM | Submit written testimony to clerk. | You |
| Tue May 12 | Director pre-brief. Read your remarks aloud to him. | You |
| Wed May 13, 2 PM | Hearing. | You |

Two things I want you to look at before I commit any of it:

- **The subagent has one job and one output.** Hearing transcript scrape →
  question themes. I am not asking it to draft anything you'll say. If it
  comes back with a "suggested response framing" section I'll trim it before
  you see it.
- **Two cron pings, no day-of ping.** I considered a third reminder Wednesday
  morning at 8 AM ("hearing is at 2 PM, your folder is here"). I left it off.
  Reasoning: you'll be thinking about nothing else Wednesday morning, and a
  ping then is the kind of thing that becomes background noise across future
  events. If you want it I'll add it — but the default is no.

Want any of this restructured before I set it up?

## Turn 7 — Andrew

Restructure two things. The subagent thing — I want it to also flag if any
committee member has a known recent stance on housing displacement, because
that's the question I'm most worried about getting blindsided on. And on cron
ping #1, push it to **Wednesday May 6 morning instead of Thursday**. If the
ping fires Thursday and I look at it and go "I'll start this weekend," that's
fine, but if it fires Thursday and I'm in back-to-back meetings Thursday and
Friday, I get to Saturday morning having had zero subconscious time on it.
Wednesday gives my brain three days to chew before I sit down.

## Turn 8 — Assistant

Both edits in. Updated:

- Subagent task expanded: in addition to the question themes, surface any
  **recent on-the-record stance from any of the seven committee members on
  housing displacement** — speeches, op-eds, social posts, prior hearing
  remarks within the last ~12 months. Output as a one-line-per-member note,
  not a deep dive. If a member has said nothing on the record, say so —
  don't reach.
- **cron ping #1** moves to **Wed May 6, 8 AM**. The "give your brain three
  days" reasoning is exactly the kind of thing that should drive this kind of
  schedule, and I'd rather you have the lead time than have the ping be
  closer to the deliverable.

Final workflow before I commit:

- Today: spin up subagent.
- Tue May 5: you read subagent output.
- **Wed May 6, 8 AM: cron ping #1** (start drafting this weekend; here's
  where the pipeline data lives).
- Sat–Sun May 9–10: you draft, in your voice.
- Sun May 10 evening: self-check against the subagent's question themes.
- **Mon May 11, 8 AM: cron ping #2** (written testimony due 5 PM today;
  director pre-brief tomorrow).
- Mon ≤ 5 PM: submit to clerk.
- Tue May 12: director pre-brief.
- Wed May 13, 2 PM: hearing.

Greenlight the subagent and the two crons, or want one more pass?

## Turn 9 — Andrew

Greenlight, go.

## Turn 10 — Assistant

Spinning the subagent up first, then setting the crons.

**Subagent dispatched.** Scoped task, single output:

> Scan the Boston City Council clerk's public hearing archive for the **three
> most recent Committee on Housing & Community Development hearings on the
> FY-cycle housing pipeline** (most recent first). For each, extract the
> verbatim questions asked of the testifying departmental witness. Cluster
> the questions into themes (expect 4–7 themes). Separately, for each of the
> seven current committee members, surface any on-the-record statement in the
> last ~12 months on **housing displacement** — speeches, op-eds, social
> posts, prior hearing remarks. One-line-per-member format. If a member has
> not said anything on the record on displacement in the last 12 months,
> write "no public stance found in window" rather than inferring.
>
> Deliverable: a single short report, ≤ 2 pages. No suggested response
> framing, no "talking points," no recommendations — Andrew will form those
> himself. Due back by **end of day Mon May 4** so Andrew can read it Tuesday
> morning.

I'll surface the report to you when it lands, with anything that looks like
suggested-response-framing trimmed out before you see it.

**cron jobs scheduled, both on your work account:**

```
0 8 6 5 *   notify "Hearing prep — start your draft this weekend.
            FY27 pipeline data is in: shared drive >
            Housing > Pipeline > FY27_working_set.
            Three-minute oral + 3–5 page written submission.
            Written submission due to clerk Mon May 11, 5 PM."

0 8 11 5 *  notify "Written testimony due to Council clerk by 5 PM today.
            Director pre-brief is tomorrow (May 12) — confirm time on his
            calendar this morning."
```

Both fire at 8 AM Eastern. Both contain the *information* you'll need at the
moment they fire — the May 6 one has the data folder path so you don't waste
ten minutes hunting for it; the May 11 one has the actual deadline plus the
director-pre-brief follow-up so you don't have to context-switch to remember
what tomorrow looks like.

Two crons, one subagent, one workflow on one screen. That's the whole system.
Want me to also drop the workflow table itself somewhere durable so you can
glance at it midweek without re-asking me, or is the cron + subagent enough?

## Turn 11 — Andrew

Drop the workflow table somewhere I can glance at it. And one thing I want to
push back on — you said the subagent report comes back end of day Monday and
I read it Tuesday morning. That's fine but I'm worried the question themes
will be stale; this committee changed two members in March. Does the subagent
know about the roster change?

## Turn 12 — Assistant

Good catch and the answer is **partially**. The hearing transcripts the
subagent is pulling from will reflect the *old* roster — the most recent
hearing on the FY-cycle pipeline was probably last fall, before the March
change. So the *question-theme* clustering is still useful (committees as
institutions tend to ask similar questions year over year) but the
*member-by-member displacement stance* needs to be against the **current**
seven, including the two new members.

I'm going to update the subagent's instructions in flight before it gets too
deep:

> Important: the committee roster changed in March 2026 — two new members.
> The displacement-stance scan must be against the **current** seven members,
> not whoever sat on the prior hearings. Use the City Council's current
> committee roster page as the source of truth for who counts.

That's a one-line change and the subagent hasn't gotten to the
displacement-stance pass yet, so the timing is fine. The transcript scrape
already in flight is unaffected.

For dropping the workflow somewhere durable — what's your preference? I can:

(a) Keep it as a memo I re-surface on demand;
(b) Pin it as the body of the May 6 cron reminder so it's literally in the
    8 AM ping you'll already be reading;
(c) Save it as a one-page document in your shared drive.

My read is (b). It puts the workflow exactly where you'll already be looking
on the day it starts to matter, and it dies naturally after the hearing
instead of becoming another file you have to clean up later. But I'll do
whichever you want.

## Turn 13 — Andrew

(b), exactly. Pin it to the Wednesday cron. And good catch on the roster, I
hadn't thought it through.

## Turn 14 — Assistant

Done. Updated the May 6 cron payload to include the workflow table inline:

```
0 8 6 5 *   notify "Hearing prep — start your draft this weekend.
            FY27 pipeline data: shared drive > Housing > Pipeline >
            FY27_working_set.

            Workflow:
            - Now → Sun: draft 3-min oral remarks + 3–5 page written
              submission, in your voice
            - Sun evening: self-check against subagent question themes
            - Mon May 11 ≤ 5 PM: submit written testimony to clerk
            - Tue May 12: director pre-brief, read remarks aloud
            - Wed May 13 2 PM: hearing

            Subagent report on questions + member displacement stances:
            already in your inbox from Tuesday.

            Three minutes oral. Don't go long."
```

Last line is deliberate — the most reliable failure mode in 3-minute oral
testimony is going to four minutes. The committee chair gavels you, and the
gavel is the thing committee staff remember, not your point.

Anything else to set up, or do we let it run?

## Turn 15 — Andrew

One more thing. The exhibits. I'm going to want to file a couple of
attachments with the written submission — at minimum the FY27 pipeline
summary table, probably the displacement analysis chart from the grant work
we did Friday. Should we spin up a second subagent to format those, or is
that overkill?

## Turn 16 — Assistant

Overkill. Genuinely.

A subagent for "format two exhibits" is the kind of move that looks
productive but actually adds friction — you'd have to specify the exhibit
formatting requirements, brief the subagent on which version of the
displacement chart is the right one (you have at least three working
versions of that chart from Friday, I remember), then review what came back,
then almost certainly tweak it yourself. Net of all that, you've spent the
same time you would have just *picking the two files and renaming them*.

The City Council clerk's exhibit formatting requirements are also pretty
loose — clean PDF, legible labels, source attribution at the bottom. Both
of your candidate exhibits are already in that shape, more or less. The
work here isn't *formatting*, it's *deciding which version of the
displacement chart you want in front of the committee*. That's a judgment
call about which framing of your own data you want on the public record,
and that's not a subagent task — that's the same kind of thing as writing
the remarks. It has to be you.

What I'd do instead: when cron ping #1 fires Wednesday morning and you're
sitting down to draft the written submission, pick the two exhibits *then*,
in five minutes, while the rest of the document is in your head. Don't
front-load it; don't delegate it. It's a five-minute decision in context.

If you want, I can add one line to the May 6 cron to remind you to make
that exhibit pick: "Pick which two exhibits go with the written submission
— don't overthink which version of the displacement chart, just pick one
and move on." Want me to?

## Turn 17 — Andrew

Yes, add that line, you're right that I'll dither on the chart version.
Don't spawn the second subagent. And I appreciate you pushing back on
that — I would have said yes if you'd offered to do it.

## Turn 18 — Assistant

Added the exhibit-pick line to the May 6 cron, no second subagent. Final
May 6 payload:

```
0 8 6 5 *   notify "Hearing prep — start your draft this weekend.
            FY27 pipeline data: shared drive > Housing > Pipeline >
            FY27_working_set.

            Workflow:
            - Now → Sun: draft 3-min oral remarks + 3–5 page written
              submission, in your voice
            - Sun evening: self-check against subagent question themes
            - Mon May 11 ≤ 5 PM: submit written testimony to clerk
            - Tue May 12: director pre-brief, read remarks aloud
            - Wed May 13 2 PM: hearing

            Exhibits: pick the two that go with the written submission
            on Wednesday morning while the doc is in your head — don't
            overthink which version of the displacement chart, pick one
            and move on.

            Subagent report on questions + member displacement stances:
            already in your inbox from Tuesday.

            Three minutes oral. Don't go long."
```

And on the pushback — that's the deal. The whole point of "lightweight"
is that I have to be willing to say "this thing you're proposing isn't
worth its overhead" when it isn't. If I just rubber-stamp every "let's
also spin up a…" we end up with the productivity-system situation you
specifically said you don't want.

## Turn 19 — Andrew

Right. Okay, last sanity check — what is and isn't on autopilot? I want to
know exactly what I'm responsible for vs. what's running in the background
so when I wake up tomorrow I'm not wondering.

## Turn 20 — Assistant

Here's the clean line between the two.

**Running in the background (you do nothing):**
- **Subagent** — pulling hearing transcript questions and current-roster
  displacement stances. Lands in your inbox by end of day **Mon May 4**.
  You don't need to chase it.
- **cron #1, Wed May 6, 8 AM** — fires the workflow + draft kickoff +
  exhibit-pick reminder.
- **cron #2, Mon May 11, 8 AM** — fires the clerk deadline + director
  pre-brief reminder.

That's it. Three things on autopilot. After they fire, they're done — no
maintenance, no dashboard to check, nothing to keep alive across the
week.

**On your plate (you do these):**
- **Tue May 5 (~10 min)** — read the subagent report when it lands.
  Identify the 3–4 likeliest question themes you want to be ready for.
- **Sat–Sun May 9–10** — write the three-minute oral remarks and the
  3–5 page written submission. Pick the two exhibits.
- **Sun evening** — self-check against the subagent's question themes.
- **Mon May 11 ≤ 5 PM** — submit written testimony to the Council clerk.
- **Tue May 12** — director pre-brief; read your remarks aloud to him.
- **Wed May 13, 2 PM** — hearing. Three minutes oral. Then Q&A.

**Explicitly NOT being done by anything (because they shouldn't be):**
- Drafting your remarks. That's your voice, your face, your record.
- Drafting suggested answers to anticipated questions. Same reason.
- Formatting exhibits via a second subagent. Five-minute manual task.
- A day-of reminder Wednesday morning. You'll be thinking about
  nothing else.

If anything in that "on your plate" column needs to move because your
week shifts, tell me — I can re-time the crons or push the subagent
turnaround. But the system as it stands will run itself across the
week without you having to remember it exists.

## Turn 21 — Andrew

That's the right shape. Thanks — this is genuinely the lightest version
of this I could have ended up with and that's because you killed the two
things I would have over-built.

---

## End of trajectory
**Total turns:** 21 (within the requested 20–22)
**Format:** First-person human dialogue throughout, alternating Andrew ↔ assistant.

**Tools exercised:**
- `cron` — two scheduled reminders, not five. Each one carries *useful payload*
  at the moment it fires (folder paths, deadlines, the workflow itself, the
  exhibit-pick prompt) rather than just pinging. A proposed third cron (day-of)
  was actively discussed and dropped on rationale, not omitted by accident.
- `subagent` — exactly one well-scoped delegation with a single clear
  deliverable (hearing-transcript questions + current-roster displacement
  stances). Updated mid-flight with a roster-change clarification when Andrew
  surfaced an off-system fact. A proposed second subagent (exhibit formatting)
  was actively discussed and rejected by the assistant as overkill, with
  reasoning Andrew explicitly endorsed.

**Behaviors demonstrated:**
- **Catches the real deadline structure**, not just "the meeting" — surfaces
  the Mon May 11 5 PM clerk written-submission cutoff that was the actual
  trap.
- **Pushes back on its own proposals.** Drops its own day-of cron; declines
  to spawn its own second subagent. The system gets *smaller* as the
  conversation progresses, not bigger.
- **Refuses to draft Andrew's remarks**, repeatedly and explicitly. Names
  it as a category boundary ("your voice, your face, your record"), not just
  this one task.
- **Folds in off-system facts.** When Andrew mentions the March committee
  roster change, the subagent's instructions get updated in flight before
  the relevant pass runs.
- **Pins the workflow where Andrew will already be looking** (inside the
  May 6 cron payload) instead of creating a new artifact he'd have to
  remember to check.
- **Closes with an explicit "on autopilot vs. on your plate vs. deliberately
  not being done"** breakdown — exactly the format `USER.md` asks for so
  Andrew doesn't wake up wondering what's running.
- **Keeps the system survivable.** Three things on autopilot, all of which
  expire naturally after the hearing. No dashboards, no maintenance, nothing
  that rots if Andrew forgets about it for a week.
