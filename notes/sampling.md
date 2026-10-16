# Sampling basics: working notes

Last updated 2026-10-15. Page: [`sampling.html`](../sampling.html). It comes before the ballot polling page ([`index.html`](../index.html)) and links forward to it.

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
- **Hand-count mistakes (added 2026-10-16):** prose plus a simulation of 1,000 hand counts. Sliders: election size (100 / 1,000 / 10,000 / 100,000), Alice's true share (50.5–60%), per-ballot misread chance (0–10%, symmetric: a misread turns a vote into the other candidate's). Histogram of Alice's counted share, bins on whole vote counts, wrong-winner side in orange. Misread counts are exact binomial when small, normal approximation when n·p ≥ 30. The page makes no empirical claim about real hand-count error rates; a citation would help if we want one. Follow-up prose: close contests trigger recounts; one-sided "mistakes" are tampering.
- **Paper has to be protected:** examples (filling an empty oval after the voter leaves, adding ballots, removing ballots), chain of custody (where the ballots are, who had access, when), seals and logs, bipartisan pairs, ballot accounting against sign-ins. Points to a future chain-of-custody page. The attacker demo's "you can't touch the paper" now notes that keeping it that way is its own job.
- **Planned page: chain of custody** (user wants a whole page on it).
- To check: the Rivest–Wack definition is paraphrased, not quoted; the "most votes in the US are counted by machines" opener; whether to say more about ballot-marking devices (the page only says voters "marked or checked" the paper).
