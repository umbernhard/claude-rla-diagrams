# RLA diagrams

Interactive diagrams for explaining risk-limiting audits, worked out alongside [rlamath](https://github.com/umbernhard/rlamath).

## Ballot polling

[`index.html`](index.html) shows ballot polling audits as stacks of ballot sequences ("ballot landscapes"):

- **Six ballots:** every sequence of a 4–2 election drawn as a path, stacked into towers, and compared with a 3–3 tie.
- **1,000 ballots:** the same steps at scale, where the stacks become a ridge of bell curves.
- **Evidence chart and simulations:** the SPRT likelihood ratio as an audit runs, and how often audits stop early when the result is right or wrong.

The page is a single self-contained HTML file. Open it in a browser, or turn on GitHub Pages (Settings → Pages, deploy from the `main` branch) to serve it.

## Notes

[`notes/ballot-polling.md`](notes/ballot-polling.md) has the math behind the page, design decisions, corrections found in the rlamath notebooks, and next steps for comparison audits.
