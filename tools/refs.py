"""Renumber citations on a page.

Citations in the text are written as <sup class="fn" data-ref="KEY">...</sup>,
or as the placeholder [[KEY]]. References live in <section class="refs"> as
<li data-ref="KEY">...</li>. This script numbers citations in order of first
appearance, rewrites each <sup>, and reorders the reference list to match.
Unused references are dropped; a citation with no reference is an error.

Usage: python3 tools/refs.py page.html [more.html ...]
"""
import re, sys

SUP = re.compile(r'<sup class="fn" data-ref="([\w-]+)">.*?</sup>|\[\[([\w-]+)\]\]')
LI = re.compile(r'<li[^>]*data-ref="([\w-]+)"[^>]*>(.*?) <a href="#cite[\w-]*" aria-label="Back to text">↩</a></li>', re.S)
REFS = re.compile(r'(<section class="refs"[^>]*>\s*<h2[^>]*>.*?</h2>(?:\s*<p[^>]*>.*?</p>)?\s*<ol>)(.*?)(\s*</ol>)', re.S)

def renumber(path):
    s = open(path).read()
    m = REFS.search(s)
    if not m:
        raise SystemExit(f'{path}: no references section')
    bodies = {k: v for k, v in LI.findall(m.group(2))}
    head, tail = s[:m.start()], s[m.end():]
    order, seen = [], set()
    def sub(mm):
        key = mm.group(1) or mm.group(2)
        if key not in bodies:
            raise SystemExit(f'{path}: citation [{key}] has no reference')
        first = key not in seen
        if first:
            seen.add(key); order.append(key)
        n = order.index(key) + 1
        idattr = f' id="cite-{key}"' if first else ''
        return f'<sup class="fn" data-ref="{key}"><a href="#ref-{key}"{idattr} aria-label="Reference {n}">{n}</a></sup>'
    head = SUP.sub(sub, head)
    items = ''.join(f'\n      <li id="ref-{k}" data-ref="{k}">{bodies[k]} <a href="#cite-{k}" aria-label="Back to text">↩</a></li>' for k in order)
    s = head + m.group(1) + items + m.group(3) + tail
    open(path, 'w').write(s)
    dropped = sorted(set(bodies) - seen)
    print(f'{path}: {len(order)} references' + (f'; dropped unused: {", ".join(dropped)}' if dropped else ''))

for p in sys.argv[1:]:
    renumber(p)
