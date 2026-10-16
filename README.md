# RLA diagrams

Interactive diagrams for explaining risk-limiting audits, worked out alongside [rlamath](https://github.com/umbernhard/rlamath).

## Sampling basics

[`sampling.html`](sampling.html) is the starting point for readers new to the statistics:

- **An election as a picture:** counting ballots as steps on a grid, and every order of the same ballots ending at the same result.
- **Why mix the ballots:** an unshuffled box can mislead a partial read; people are bad at randomness; seeded pseudo-random number generators, with interactive demos.
- **What a sample can say:** every order of a small election, sampling distributions from many shuffles, and which results could have produced a given sample, ending at the tie.

## Ballot polling

[`index.html`](index.html) shows ballot polling audits as stacks of ballot sequences ("ballot landscapes"):

- **Six ballots:** every sequence of a 4–2 election drawn as a path, stacked into towers, and compared with a 3–3 tie.
- **1,000 ballots:** the same steps at scale, where the stacks become a ridge of bell curves.
- **Evidence chart and simulations:** the SPRT likelihood ratio as an audit runs, and how often audits stop early when the result is right or wrong.

The page is a single self-contained HTML file. Open it in a browser, or turn on GitHub Pages (Settings → Pages, deploy from the `main` branch) to serve it.

## Notes

[`notes/sampling.md`](notes/sampling.md) covers the sampling page: its structure, the feedback behind it, and open items, including a planned page on software independence.

[`notes/ballot-polling.md`](notes/ballot-polling.md) has the math behind the page, design decisions, corrections found in the rlamath notebooks, and next steps for comparison audits.
