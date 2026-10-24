# RLA diagrams

Interactive diagrams for explaining risk-limiting audits, worked out alongside [rlamath](https://github.com/umbernhard/rlamath).

> **Under construction, made with AI.** Much of this site was written and coded with help from an AI model (Claude) and hasn't been fully checked. It may contain errors; every page carries a banner saying so. Pages the author has reviewed (so far, the why-paper page) say so in their banner; the rest are still drafts.

[`index.html`](index.html) is the landing page: it lists the parts in reading order (0 why paper, 1 sampling basics, 2 ballot polling) and the planned pages.

## Why paper

[`why-paper.html`](why-paper.html) comes first: why audits check paper ballots rather than electronic records (software independence).

- **One vote, two records:** a slider makes the software record some Alice votes as Bob; a hand count of the paper shows the true result, and switching to "No paper" shows that recounting the same records proves nothing.
- **Try to change the outcome:** the reader edits electronic records to make Bob win, then hand counts the paper, which finds the true outcome every time. 
- **Imperfect hand counts and protecting the paper:** a simulation of 1,000 hand counts with misreads shows how rarely honest counting mistakes change a winner, then a section on tampering with paper and chain of custody. The page closes on the cost of full hand counts, leading into the sampling page.

## Sampling basics

[`sampling.html`](sampling.html) is the starting point for readers new to the statistics:

- **An election as a picture:** counting ballots as steps on a grid, and every order of the same ballots ending at the same result.
- **Why mix the ballots:** an unshuffled box can mislead a partial read; people are bad at randomness; seeded pseudo-random number generators, with interactive demos.
- **Know what you're drawing from:** building a ballot manifest and drawing ballots from it with a public seed, then a fixed-percentage audit with a wrong manifest (a container left off, a count too low, a count too high).
- **What a sample can say:** every order of a small election, sampling distributions from many shuffles, and which results could have produced a given sample, ending at the tie.

## Ballot polling

[`ballot-polling.html`](ballot-polling.html) (part 2, older draft being reworked) shows ballot polling audits as stacks of ballot sequences ("ballot landscapes"):

- **Six ballots:** every sequence of a 4–2 election drawn as a path, stacked into towers, and compared with a 3–3 tie.
- **1,000 ballots:** the same steps at scale, where the stacks become a ridge of bell curves.
- **Evidence chart and simulations:** the SPRT likelihood ratio as an audit runs, and how often audits stop early when the result is right or wrong.

The page is a single self-contained HTML file. Open it in a browser, or turn on GitHub Pages (Settings → Pages, deploy from the `main` branch) to serve it.

## Reading list

[`references.html`](references.html) collects every source cited in the series plus the wider literature on election audits and voting system security, grouped by topic, with a search filter. It is generated from [`bib/references.json`](bib/references.json) by `python3 tools/build_reading_list.py` (template: `tools/reading_list_template.html`); edit the JSON, not the HTML. Each entry records where its details came from (`source`). The build fails if a page cites a key that isn't in the bibliography.

## Citations

Citations are written as `<sup class="fn" data-ref="KEY">` (or the placeholder `[[KEY]]`) with a matching `<li data-ref="KEY">` in the page's References section. Run `python3 tools/refs.py page.html` after editing to renumber citations in order of appearance and reorder the list.

## Notes

[`notes/sampling.md`](notes/sampling.md) covers the sampling page: its structure, the feedback behind it, and open items, including a planned page on software independence.

[`notes/ballot-polling.md`](notes/ballot-polling.md) has the math behind the page, design decisions, corrections found in the rlamath notebooks, and next steps for comparison audits.
