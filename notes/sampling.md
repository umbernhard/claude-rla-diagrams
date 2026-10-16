# Sampling basics: working notes

Last updated 2026-10-15. Page: [`sampling.html`](../sampling.html). It comes before the ballot polling page ([`ballot-polling.html`](../ballot-polling.html)) and links forward to it.

## Why this page exists

- After Mark Lindeman's feedback, the series is aimed at curious non-statisticians (Numberphile / 3Blue1Brown style). It starts as simply as possible, uses only 2D drawings, and doesn't treat the reported result or likelihood ratios as necessary.
- Mark's points it responds to: the 3D towers fought his intuition (2D paths and frequency bars worked better; he likes contour maps); "reading one ballot tells us nothing" was wrong and is now explicitly contradicted; LRs shouldn't be presented as inevitable (tie-only tests, e.g. Stark's martingale approaches, are valid too). He is interested in extending this to Athena/Minerva tail LRs.

## Sections, in order

1. **An election, drawn as a picture.** Two candidates; a result is a point; each Alice ballot is a step right, each Bob ballot a step up. Figure: count ten ballots (6–4), with "Alice has more" / "Bob has more" halves, the tie line, and the ten-ballot line. "Count in a different order" shows a different path to the same point.
2. **There is no order of voting.** Figure: all 210 orders of the 6–4 election, edge width and opacity scaled by how many orders use each edge, counts at points, "Trace one order". Every path is the same outcome. Order would not matter in a full count; it only matters because the audit avoids reading every ballot where possible.
3. **Reading a box that hasn't been mixed.** 40 ballots stacked by precinct (Bob-leaning precinct first) vs shuffled.
4. **Mix first, then draw.** Shuffling makes unrepresentative pockets less likely (not impossible). Pick-a-number demo: first pick ("we guessed 7 or 2"), then 30 picks compared with 30 fair-die rolls, counting repeats (about 3 expected). PRNG text (user's wording). Twin seeded generators: same seed → identical streams; one changed character → unrelated streams, ~1 in 10 positions match by chance. Guess-the-next-number game with a secret seed, then replay from the revealed seed. Ballot manifest and public dice seed (Colorado). Drawing one at a time is as fair as all at once.
5. **Six ballots, every possible order.** All 15 orders of a 4–2 election; slider highlights a diagonal and a bar chart shows how the 15 orders split there (sampling distribution).
6. **A box of 100, shuffled 200 times.** Paths, crossing dots, histogram vs exact hypergeometric, middle-90% band. Spread in counts grows then shrinks; spread as a share shrinks throughout.
7. **Turning the question around / which boxes could have produced this sample?** 1,000-ballot box; for every possible Alice count, the chance of exactly this sample; tie and reported marked; tail under the tie. One Alice ballot turns the curve into a ramp.
8. **The result that matters.** Ruling out the tie is enough; two ways to argue against it (surprise under a tie alone, or comparison with the reported result); checking after every ballot needs care → next page.

## Demo PRNG

- Number i from seed s is SHA-256("s,i") (first 6 bytes, reduced mod 10) + 1, via `crypto.subtle`. Checked: deterministic, even across 1–10. It illustrates the seed-plus-counter idea but is not any official audit tool's algorithm.

## Wording

- Avoid the word "fix" in election writing (it can imply fraud).

## Open items

- Connect PRNG output to choosing a ballot from the manifest (deliberately left for later).
- Check the claim that Colorado's seed is rolled after the manifest is final.
- Simplifications to relax later: two candidates, no invalid ballots, sampling without replacement.
- Rework the ballot polling page: drop what this page now covers, revisit the towers, avoid framing the LR as required.

## Why paper page (software independence), built 2026-10-15

- Page: [`why-paper.html`](../why-paper.html), Part 0, links forward to this page; this page links back to it from the intro.
- Built from these two demo ideas: (1) a machine screen says Alice, the electronic record says Bob, the paper the voter checked says Alice; a slider flips some share of electronic records, the reported result moves, the paper doesn't, and sampling the paper catches it. (2) "Hack the count": try to change the outcome by editing only electronic records; every attempt shows up when the paper is sampled.
- Both demos use 100 voters, 55–45 on paper; 6 changed records flip the reported winner (5 makes a tie). The page only talks about full hand counts, so the next page can motivate sampling: demo 1 is a hand count of the paper vs a recount of the records ("No paper"); demo 2 lets the reader edit records, then hand count the paper, which always undoes the changes. The closing says hand counts are the gold standard but slow, and asks whether some of the paper could give most of the confidence.
- **Hand-count mistakes (added 2026-10-16):** prose plus a simulation of 1,000 hand counts. Sliders: election size (100 / 1,000 / 10,000 / 100,000), Alice's true share (50.5–60%), per-ballot misread chance (0–10%, symmetric: a misread turns a vote into the other candidate's). Histogram of Alice's counted share, bins on whole vote counts, wrong-winner side in orange. Misread counts are exact binomial when small, normal approximation when n·p ≥ 30. Now cited: Goggin, Byrne & Gilbert 2012 (ELJ 11(1):36–51, doi:10.1089/elj.2010.0098; checked against the PDF: lab study, 108 volunteers in groups of 3–4, stacks of 120 mock ballots, 46.7% of groups miscounted at least one candidate, mean candidate-count error 1.4%, read-and-mark 0.48%, sort-and-stack 2.13%; wrong-vote errors couldn't be measured separately because only totals were recorded) and Ansolabehere et al. 2018 (ELJ 17(2); Wisconsin recounts, 0.21% and 0.59% absolute differences, scanners more accurate than hand counts). Follow-up prose: close contests trigger recounts; one-sided "mistakes" are tampering.
- **Paper has to be protected:** examples (filling an empty oval after the voter leaves, adding ballots, removing ballots), chain of custody (where the ballots are, who had access, when), seals and logs, bipartisan pairs, ballot accounting against sign-ins. Points to a future chain-of-custody page. The attacker demo's "you can't touch the paper" now notes that keeping it that way is its own job.
- **Planned page: chain of custody** (user wants a whole page on it).
- References added 2026-10-16 (numbered notes + References list on both pages): Rivest 2008 / Rivest & Wack 2006 (definition now quoted exactly), Goggin et al. 2012, Ansolabehere et al. 2018, EAC chain of custody best practices 2021, Stark & Wagner 2012 (compliance audits), Colorado SOS seed notice (20+ digits, ten-sided die, public rolls, after Election Day). The sampling page no longer claims the seed comes after the manifest is final; the notice doesn't say.
- To check: the "most votes in the US are counted by machines" opener; whether to say more about ballot-marking devices (the page only says voters "marked or checked" the paper).

## Site structure (2026-10-16)

- `index.html` is a landing page; the old ballot polling page moved to `ballot-polling.html`. Every page has an "Under construction · Made with AI · May contain errors" banner (self-contained CSS, hazard stripe) with a link back to the landing page.

## Sources pulled 2026-10-16 (read via web, not downloaded)

- **Atkeson, Alvarez & Hall, New Mexico 2006 Post Election Audit Report (rev. Oct 2009).** Bernalillo County, audit Feb–Mar 2008, ~25% sample (47,481 ballots, 107 of 423 precincts). First machine count vs 2-person / 3-person hand counts: average differences 0.19% / 0.13%; 76% of Election Day batches identical, 9% off by one vote, rest off by 2–3 at most; differences "does not favor one candidate or party"; machine-to-machine agreement better than hand-to-hand. Checked against the PDF (user uploaded as zip): machine vs first hand count identical in 76% of Election Day, 52% absentee, 61% early batches (p. 51); two hand counts identical in >70% of Election Day and early batches, 45% absentee, max 6 ballots off any count, aggregate differences ≤0.3% per candidate, net deviations random and canceling (pp. 61–63, Tables 3.7–3.8). Goggin et al.'s "45–64%" seems to come from an earlier version; the 2009 report says 45% to over 70%.
- **Ansolabehere & Reeves 2004, VTP Working Paper 11.** NH recounts 1946–2002: hand counts ~0.83% historical discrepancy, 2002 hand 0.87% vs scanner 0.56%; races under ~0.5% have a non-trivial chance of reversal; suggest 0.5% as a minimum automatic-recount threshold.
- **Rhode Island RLA pilot report (Brennan Center, Sept 2019).** Jan 2019 pilots: ballot comparison (Bristol, 100 ballots, measured risks ~0.3–0.5%), ballot polling (Portsmouth, 200 ballots, governor; sample 99–69, margin 15.7% vs reported 22.2%; measured risk 10.2%, so a 10% risk limit would have required continuing), batch comparison (two precincts, sort-and-stack vs hashmarking; final counts matched originals exactly after recounts). Seed: observers rolled 20 ten-sided dice in public, 14 minutes. Timing per ballot and manifest errors (a precinct typed 0025 for 0205) are good material for the chain-of-custody and comparison pages. Recommends ballot-level comparison audits.
- **Mebane & Bernhard 2018, Voting '18 (FC workshops).** 2016 WI and MI recounts: zero change the most common ward outcome for hand, machine and mixed recounts in WI; largest changes tied to nonstandard pens/ballots and tabulator error; Table 5: lost ballots cited in 23 wards, ballots found during recount in 72 (now cited in the why-paper custody section); about half of WI votes were recounted by machine; MI recount entirely manual; conclusion recommends an RLA or full manual retabulation for evidence the counts are right.
