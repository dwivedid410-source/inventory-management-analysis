# User Trajectory — Resident Complaint Tracking Dashboard

**Persona:** Andrew, Deputy Director of Community Development, City of Boston.
Manages constituent engagement and complaint resolution. Reports to a Director.
Coworker Imran handles code enforcement complaints. Andrew can follow along
with spreadsheet work but isn't deeply technical. Today is Wednesday;
deliverable is due Friday.

Format: 14 turns, first-person user voice only. No assistant replies.

---

## Turn 1
so i just pulled this csv from our complaint tracking system and its a mess. like 800+ rows going back to july of last year. columns are all over the place, some have dates in different formats, theres duplicate entries.. i need to actually make sense of this data because my director asked me for a summary of complaint trends by neighborhood and i told her id have it by friday. its wednesday. can you take a look at this and help me figure out what we're working with? ill upload it in a sec

## Turn 2
ok here it is — `complaints_FY_export.csv`. before you dig in, couple things i already noticed scrolling through it: the "neighborhood" column has stuff like "Dorchester", "DOT", "dorchester " with a trailing space, and just blanks. and the date column?? some are 7/14/2025, some are 2025-07-14, and i swear i saw one that just said "July". so yeah. dont trust anything yet. just give me like a top-level read first — how many rows actually, how many unique complaints once you dedupe, what columns we have, whats usable and whats garbage. dont start charting yet i wanna see the lay of the land

## Turn 3
ok that helps. 812 rows, 47 likely dupes, 11 columns — got it. on the duplicates though, before you just drop them: are those exact dupes or like same address + same date + same category? because honestly people DO call twice about the same pothole and i dont want to undercount the real complaint volume. can you split that out? show me how many are true exact duplicates vs how many are "same issue same address within a few days" — i think those are different things. the first one we drop, the second one we keep but maybe flag

## Turn 4
yeah ok keep the near-dupes, drop the exact ones. now the dates. can you just normalize everything to ISO format and add a column for fiscal_month and fiscal_quarter? boston FY runs july to june fyi, so july = month 1 of FY26. and any rows where the date is unparseable — dont delete them, put them in a separate "needs review" tab/sheet so i can eyeball them later. director hates when stuff just disappears from totals without explanation

## Turn 5
neighborhood column is gonna be the worst part i think. can you build a mapping — like "DOT" "dot" "Dorchester " all collapse to "Dorchester", "JP" to "Jamaica Plain", "ESB" to "East Boston", etc. use the official 23 boston neighborhoods as the canonical list. anything that doesnt map, bucket as "Unspecified" but also tell me the count of unspecified so i can flag if its a problem. if its like 5 rows fine, if its 80 rows we have a data entry issue i need to raise

## Turn 6
hm 64 unspecified is too many. before we move on can you show me the raw values that ended up in unspecified? i bet half of them are actual neighborhood names just spelled weird or its a street address instead of a neighborhood. i can probably eyeball-fix most of them and we can re-map. also some of those might be from the airport or harbor stuff that legitimately isnt a neighborhood — those should be their own bucket called "Citywide/Other"

## Turn 7
ok much better, 12 unspecified now, ill live with that. now lets actually look at the data. give me:
- complaints per month over the FY (so i can see the trend line)
- top 5 categories overall
- top 3 categories per neighborhood for the 8 highest-volume neighborhoods
- avg days to resolution by category (if theres a closed_date column? i think there is)

put it all in an xlsx workbook with a tab per view. dont make it pretty yet just get the numbers right first

## Turn 8
wait before charts — the resolution time numbers look off. some are negative?? thats not possible unless closed_date is before opened_date. how many rows have that and can we just null those out for the resolution calc but keep the row for volume counts? and whats the median resolution time not just average, average is gonna be skewed by that one complaint thats been open 287 days lol

## Turn 9
ok now charts. for the director memo i want:
1. a clean line chart of complaints per month
2. a horizontal bar chart of top categories
3. a heatmap-ish thing of neighborhood x category — or actually maybe just a stacked bar by neighborhood would be more readable for her. she doesnt love heatmaps
4. and a small kpi-style block at the top: total complaints, % resolved, median resolution days, top neighborhood by volume

keep the colors muted/professional, no rainbow stuff. boston city blue if you can match it but its not critical

## Turn 10
actually one more cut i want to look at — are there any neighborhoods where complaint volume jumped significantly in the last 2-3 months vs the FY average? thats the kind of thing the director will ask about and i dont want to be caught flat-footed. flag any neighborhood with >50% increase in recent quarter vs prior quarters and tell me the categories driving it. that might actually be the most important slide honestly

## Turn 11
mattapan jumped 78% on illegal dumping?? ok that is going in the memo for sure. and roxbury up on noise complaints, fine that tracks with summer. let me think about how to frame this. director wants "data-driven" but she doesnt want a wall of numbers, she wants like 3 clear takeaways. can you draft a 1-page memo in word — keep it to: brief intro paragraph, 3 key findings as bullets with the numbers, one short paragraph on what im recommending we do about mattapan specifically, and then "full data attached" at the bottom. tone should be confident but not overselling, shes sharp shell see through fluff

## Turn 12
the draft is close but two things — first paragraph is too long, cut it in half, she reads like the first 2 sentences and decides if she keeps reading. and dont say "constituents are increasingly concerned" you have no idea if theyre concerned, you only know they called. say "complaint volume increased". also can you add the date and address it to "Director [LASTNAME]" with brackets so i can fill that in, im blanking on the spelling honestly and dont wanna get it wrong in the file

## Turn 13
ok memo is good. now i need to send the code enforcement slice to imran — hes the one who actually closes those out and hell want a heads up about the mattapan dumping spike before director asks him about it. can you pull just the code enforcement category rows into a separate small xlsx, just those, with the same neighborhood/month breakdown? and draft a gmail to him — keep it casual, hes a friend, something like "hey imran heads up, pulled this for the director, mattapan illegal dumping is up a lot, wanted you to see before the friday meeting, lmk if the numbers track with what youre seeing on the ground". his email is imran.s@boston.gov i think. attach the xlsx

## Turn 14
perfect. one last thing — save the cleaned dataset (the deduped, normalized one) as `complaints_FY_clean.csv` so next quarter when i do this again i can just pick up from there instead of redoing all the neighborhood mapping. and remember the mapping rules we built — the neighborhood aliases especially — because i guarantee the next export will have the same garbage in it. ok i think im good. let me look everything over before i send anything to imran or the director, dont fire off that gmail yet just leave it as a draft
