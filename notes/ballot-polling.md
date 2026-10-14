# Ballot polling super diagrams: working notes

Last updated 2026-10-13. This work builds on `Old/Geometry of Post-election Audits.ipynb` in [umbernhard/rlamath](https://github.com/umbernhard/rlamath) (the triangle outcome plane and election vectors).

## Where things are

- **Interactive page:** [`index.html`](../index.html) in this repo. It is one self-contained HTML file with no build step: open it in a browser, or turn on GitHub Pages to serve it.
- **Drafts:** a private copy is also published as a claude.ai artifact, and a copy is kept in the "RLA Math" Claude project.

## The core idea: the super diagram

- Each ballot is a unit step: Alice = (1, 0), Bob = (0, 1), invalid = (0, 0). One ordering of the ballots is a lattice path from the origin to the result (V_A, V_B).
- The **super diagram** stacks every ordering that ends at the same result.
- With V = V_A + V_B valid ballots, the number of orderings passing through (a, b) is C(a+b, a) · C(V−a−b, V_A−a), out of C(V, V_A) in total.
- The **share** of orderings passing through (a, b) is C(V_A, a) · C(V_B, b) / C(V, a+b). That is the hypergeometric pmf. Invalid ballots don't move the path, so they drop out.
- A random sample of m ballots is the first m steps of a uniformly random ordering. So the share through (a, b) equals P(the sample has a Alice and b Bob votes | this result).
- Every ordering crosses each diagonal a + b = k exactly once, so each diagonal slice sums to 1. Slices are bell curves, approximately normal for large k.
- The spread of the margin across the stack at depth k is k · σ² · (N−k)/(N−1). It pinches to zero at both ends (the finite population correction): every path starts at the origin and ends at the result.

## How the SPRT falls out

- **Null:** a tie with the same number of invalid ballots and the valid ballots split evenly (Bob gets the extra vote if the valid count is odd). Beating the tie is enough, because any Bob-wins result puts even fewer paths near a sample that favors Alice.
- **Likelihood ratio = height of the reported super diagram at the sample point ÷ height of the tie super diagram there.** Sequentially, each Alice ballot multiplies the ratio by (V_A − a)/(T_A − a), and each Bob ballot by (V_B − b)/(T_B − b). Checked numerically: the height ratio matches the sequential LR to about 1e-13.
- Stop when LR ≥ 1/α, i.e. log LR ≥ log(1/α).
- BRAVO is the with-replacement approximation: (2p)^a (2−2p)^b with p = V_A/(V_A + V_B). It matches closely while the sample is a small share of the election.
- **Simulations** (N = 1,000; 600 / 300 / 100 invalid; α = 0.05):
  - Ballots as reported: the exact (without-replacement) test stopped at a median of 43 ballots. BRAVO needs about 59.
  - Ballots actually a tie: 4.45% of audits wrongly confirmed Alice, under α as required.

## Overlap between the two bells

- At depth k, overlap = Σ over the diagonal of min(P_reported, P_tie). One minus the overlap is the total variation distance between the two sampling distributions.
- The overlap depends only on k and shrinks as the sample grows. For 600 / 400 vs a 500 / 500 tie it is about 90% after 1 ballot, 52% after 40, and 35% after 80.
- This gives a precise statement: an audit can only stop quickly once the bells have mostly separated.

## Page design (current version)

**Six-ballot example.** Alice 4, Bob 2, compared with a 3–3 tie: 15 vs 20 orderings. The example uses 6 ballots rather than 5 because 5 ballots can't tie.

1. **One ordering:** the arrows are the real order of the ballots, also shown as chips.
2. **All 15 orderings:** each edge's thickness is the number of orderings that use it, and each point shows its count. Tapping an ordering traces it.
3. **Stack them up:** translucent unit blocks, with each ordering adding one block to every point it passes through. Every diagonal holds 15 blocks. The "Top view" button turns the stack into a density map.
4. **Compare with a tie:** heights switch to shares, with side-by-side blue and orange towers. The text works the ratio for the current sample.

**1,000-ballot example.** Default 600 / 400 / 0, matching the Geometry notebook.

- Same four steps, using 150 random orderings and ridge slices.
- Step 4 shades the overlap grey, and the slice at the sample's depth is drawn heavier.
- "Zoom to sample" in step 4 draws only the slices the sample has already reached, so the view starts blank.

**Also on the page:**
- An evidence chart: log LR against ballots drawn, with BRAVO dashed and the stop line.
- A "Run 1,000 audits" simulation, with a switch between ballots as reported and ballots actually a tie.

**Vertical scale:** 2.4 × the peak of the middle slice, so the ends (100% at the start and end points) are clipped. Rescaling every slice to the same peak was considered and rejected, because it hides how the bells get lower and wider in the middle.

## Corrections found in the rlamath notebooks (not yet applied)

**Auditing Elections with Hypothesis Tests.ipynb**
- P(Bob won) uses `norm.pdf(0, …)`. The area from −∞ to 0 is `norm.cdf(0, …)`.
- The sample margin is plotted at 0.36. With 72 Alice / 36 Bob / 12 invalid it is 36/120 = 0.30.
- The sample curves use the spread of the whole election. For an m-ballot sample the standard deviation is σ_ballot/√m, where σ²_ballot = (p_w + p_l) − (p_w − p_l)². For 600 / 300 / 100 that is 0.81.
- The log LR is computed as `null_LR/alt_LR`, a ratio of logs. It should be the difference log L_alt − log L_null. This resolves both TODOs: "proportion vs. absolute" and "p-value crosses α before LR crosses b". The two rules are identical, since 1/LR ≤ α ⇔ log LR ≥ log(1/α).
- Corrected numbers: the 120-ballot sample gives log LR ≈ 6.67, above log 20 ≈ 3.0, so the audit stops immediately. A sample matching the reported result needs about 54 ballots (normal approximation). At 120 ballots the minimum margin to stop is 27. The "needed 130 Alice ballots" story came from the bugs.
- The `.657` cell is accidentally a markdown cell.

**Building on permutations---the Central Limit Theorem.ipynb** (invalid votes section)
- `mu*(1 - mu/n)` is correct only for 0/1 scoring. For −1/0/+1 scoring the variance is (valid votes) − μ²/n. For the 6–4 example that is 9.6, not 1.6.
- The "peakier" claim is false: ±1 scoring doubles the spread (sd 1.55 → 3.10).
- The conclusion about invalid votes still holds: the variance goes 9.6 → 9.8 → about 10 as invalid ballots are added.

**Foundations of ballot polling.ipynb** (stub): uses the same variance formula.

## Next: comparison audits

- Idea: an "error space", with ballots sampled on the x-axis and accumulated error (positive or negative) on the y-axis.
- Connect it to the error vectors in the Geometry notebook: e = audited − reported, and the outcome is wrong when the error reaches the margin.
- Show how the error space relates to the outcome-plane drawings. Not started yet.

## Open questions

- How to handle the null with invalid ballots in general. The current choice keeps the reported invalid count.
- Whether to link this page from the rlamath notebooks.
- A notebook writing up the "height ratio = likelihood ratio" derivation, next to "Foundations of ballot polling".
