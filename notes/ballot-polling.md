# Ballot polling super diagrams: working notes

Last updated 2026-10-13. This work builds on `Old/Geometry of Post-election Audits.ipynb` in [umbernhard/rlamath](https://github.com/umbernhard/rlamath) (the triangle outcome plane and election vectors).

## Where things are

- **Interactive page:** [`index.html`](../index.html) in this repo. It is one self-contained HTML file with no build step: open it in a browser, or turn on GitHub Pages to serve it.
- **Drafts:** a private copy is also published as a claude.ai artifact, and a copy is kept in the "RLA Math" Claude project.

## The core idea: the super diagram

- Each ballot is a unit step: Alice = (1, 0), Bob = (0, 1), invalid = (0, 0). One sequence of the ballots is a lattice path from the origin to the result (V_A, V_B).
- The **super diagram** stacks every sequence that ends at the same result.
- With V = V_A + V_B valid ballots, the number of sequences passing through (a, b) is C(a+b, a) · C(V−a−b, V_A−a), out of C(V, V_A) in total.
- The **share** of sequences passing through (a, b) is C(V_A, a) · C(V_B, b) / C(V, a+b). That is the hypergeometric pmf. Invalid ballots don't move the path, so they drop out.
- A random sample of m ballots is the first m steps of a uniformly random sequence. So the share through (a, b) equals P(the sample has a Alice and b Bob votes | this result).
- Every sequence crosses each diagonal a + b = k exactly once, so each diagonal slice sums to 1. Slices are bell curves, approximately normal for large k.
- The spread of the margin across the stack at depth k is k · σ² · (N−k)/(N−1). It pinches to zero at both ends (the finite population correction): every path starts at the origin and ends at the result.

## How the SPRT falls out

- **Why the tie suffices (same invalid count):** the Alice-ballot factor (V_A − a)/(T_A − a) is always ≥ 1 and the Bob-ballot factor (V_B − b)/(T_B − b) is always ≤ 1. Any null result with the same invalid count is the tie with some Alice ballots turned into Bob ballots, which lowers the expected step, so the LR is a supermartingale under every such null and Ville's inequality still gives risk ≤ α. Nulls with a different invalid count are not covered by this argument (moving ballots to/from invalid can raise the expected step slightly); BRAVO conditions on valid ballots instead.
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

## Before any audit: every possible election

Stack every sequence of N ballots, not just the sequences of one result. Then reading a ballot rules out every sequence that started differently, halving the count each time. What happens to the possible futures depends on how the sequences are weighted:

1. **Every sequence equal.** The weight through (a, b) is C(a+b, a) · 2^(N−a−b), which fans out from the origin along the tie line. Final results are Binomial(N, ½), peaked at a tie. The unread ballots stay independent coin flips, so the final result is the sample plus Binomial(N−k, ½). The sample only uses up ballots; it never says how the rest lean. This is the permutation notebook's model, and it is why that approach needs nearly a full count.
2. **Every result equal** (then every sequence within a result): the old triangle-area model. Given a sample with a Alice and b Bob votes in k ballots, the posterior over the final Alice count F is ∝ C(N−k, F−a)/C(N, F). The sample does shift the future toward what was seen. This is Bayesian reasoning with a uniform prior over results. It is related to, but not the same as, the Bayesian audits defined in the literature (e.g. arXiv:1902.00999), so the page no longer calls it a Bayesian audit.
3. **The RLA** uses neither weighting. It compares two fixed super diagrams (reported vs. tie) through P(sample | result), never P(result | sample).

For six ballots, the chance that Alice won (final count > 3) works out as:

| Ballots read | Every sequence equal | Every result equal |
|---|---|---|
| none | 34% | 43% |
| A | 50% | 71% |
| A, A, A | 88% | 97% |

## Page design (current version)

**Every possible election (first section).** Six ballots, 64 sequences. There are buttons to read an Alice or Bob ballot, a toggle between weightings 1 and 2, lattice points shaded and labeled by the weight through them (ruled-out points shown empty), and a bar chart of possible final results.

**Six-ballot example.** Alice 4, Bob 2, compared with a 3–3 tie: 15 vs 20 sequences. The example uses 6 ballots rather than 5 because 5 ballots can't tie.

1. **One sequence:** the arrows are the real order of the ballots, also shown as chips.
2. **All 15 sequences:** each edge's thickness is the number of sequences that use it, and each point shows its count. Tapping an sequence traces it.
3. **Stack them up:** translucent unit blocks, with each sequence adding one block to every point it passes through. Every diagonal holds 15 blocks. The "Top view" button turns the stack into a density map.
4. **Compare with a tie:** heights switch to shares, with side-by-side blue and orange towers. The text works the ratio for the current sample.

**1,000-ballot example.** Default 600 / 400 / 0, matching the Geometry notebook.

- Same four steps, using 150 random sequences and ridge slices.
- Step 4 draws the slice at the sample's depth heavier. (An earlier version shaded the overlap between the two bells grey; it was removed as not very useful, but the overlap math below still holds.)
- "Zoom to sample" in step 4 draws only the slices the sample has already reached, so the view starts blank.
- **Log heights** (steps 3–4): heights become log(share), shown over a window of max(10, 2.2·log(1/α)). In step 4 the ratio at the sample becomes a vertical gap, drawn next to a green bracket of length log(1/α). The audit stops when the gap fills the bracket, which stays visible at any risk limit (linear heights fail at α = 0.01, where the orange bar would be 1% of the blue). Each bell becomes a parabola, since the log of a normal curve is quadratic.

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

## References

- M. Lindeman, P. B. Stark and V. S. Yates, "BRAVO: Ballot-polling Risk-limiting Audits to Verify Outcomes," EVT/WOTE '12, 2012. https://www.usenix.org/conference/evtwote12/workshop-program/presentation/lindeman
- A. Wald, "Sequential Tests of Statistical Hypotheses," Annals of Mathematical Statistics 16(2), 1945 (the SPRT).
- J. Ville, Étude critique de la notion de collectif, Gauthier-Villars, 1939 (Ville's inequality: a nonnegative martingale starting at 1 reaches 1/α with probability at most α).
