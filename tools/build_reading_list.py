"""Build references.html from bib/references.json.

Every citation key used on a page (data-ref="KEY") must exist in the
bibliography; entries cited on a page get a "Cited in" link back to it.

Usage: python3 tools/build_reading_list.py
"""
import html, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGES = [('why-paper.html', 'Part 0'), ('sampling.html', 'Part 1'), ('ballot-polling.html', 'Part 2')]

bib = json.loads((ROOT / 'bib/references.json').read_text())
entries = {e['key']: e for e in bib['entries']}

cited = {}
for f, label in PAGES:
    for k in dict.fromkeys(re.findall(r'<li[^>]*data-ref="([\w-]+)"', (ROOT / f).read_text())):
        if k not in entries:
            sys.exit(f'{f}: reference "{k}" is not in bib/references.json')
        cited.setdefault(k, []).append((f, label))

esc = html.escape
def render(e):
    title = esc(e['title'])
    title = f'<a href="{esc(e["url"])}">{title}</a>' if e.get('url') else title
    parts = [f'{esc(e["authors"])}, “{title},” <i>{esc(e["venue"])}</i>']
    if e.get('year'):
        parts.append(f', {e["year"]}')
    parts.append('.')
    if e.get('doi'):
        parts.append(f' <a href="https://doi.org/{esc(e["doi"])}">doi:{esc(e["doi"])}</a>.')
    if e.get('note'):
        parts.append(' ' + esc(e['note']))
    if e['key'] in cited:
        parts.append(' <span class="cited">Cited in ' + ', '.join(
            f'<a href="{f}#ref-{e["key"]}">{l}</a>' for f, l in cited[e['key']]) + '</span>')
    return f'\n        <li id="{e["key"]}">{"".join(parts)}</li>'

def year_key(e):
    return -(e.get('year') or 0)

body = []
for i, g in enumerate(bib['groups']):
    items = sorted((e for e in bib['entries'] if e['group'] == g['id']), key=year_key)
    if g['id'] == 'overview':
        items = [e for e in bib['entries'] if e['group'] == 'overview']  # curated order
    lis = ''.join(render(e) for e in items)
    inner = f'<ul>{lis}\n    </ul>'
    if g['id'] == 'ct':
        inner = f'<details>\n    <summary>Show all {len(items)} reports</summary>\n    {inner}\n    </details>'
    body.append(f'''
  <section class="group" id="{g["id"]}" aria-labelledby="h-{g["id"]}">
    <h2 id="h-{g["id"]}">{esc(g["title"])} <span class="count">{len(items)}</span></h2>
    <p class="gdesc">{esc(g["description"])}</p>
    {inner}
  </section>
''')
toc = ''.join(f'<li><a href="#{g["id"]}">{esc(g["title"])}</a></li>' for g in bib['groups'])

tpl = (ROOT / 'tools/reading_list_template.html').read_text()
out = (tpl.replace('{{COUNT}}', str(len(entries)))
          .replace('{{TOC}}', toc)
          .replace('{{BODY}}', ''.join(body)))
(ROOT / 'references.html').write_text(out)
print(f'references.html: {len(entries)} entries in {len(bib["groups"])} groups; {len(cited)} cited on pages')
