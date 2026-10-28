"""Antisèche des relais : une page A4, slide par slide, qui ouvre et la phrase
qui passe la main. Tirée des repères de scène (CUES) de slides_content.py,
donc toujours alignée sur le deck.

Usage (depuis la racine du repo) :
    uv run --with python-pptx python talks/build_relais.py
→ talks/slides/antiseche-relais.pdf (et le .html à côté). Nécessite Google Chrome.
"""
import html
import re
import subprocess
from pathlib import Path

import slides_content

ROOT = Path(__file__).parent
OUT = ROOT / "slides" / "antiseche-relais"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# Cyan / violet : les couleurs GroupBees, une par speaker.
WHO = {"M": ("Mazlum", "#06B6D4"), "G": ("Guillaume", "#8B5CF6")}
BOTH = ("chacun", "les deux", "un point chacun", "démo")


def speakers(cue_line: str) -> list[str]:
    """Speakers of a slide, in speaking order, from its « 🎤 » line."""
    text = cue_line.removeprefix("🎤").strip().lower()
    if text.startswith(BOTH):
        return ["M", "G"]
    order = [name[0].upper() for name in re.findall(r"mazlum|guillaume", text)]
    # « Mazlum, puis Guillaume, Mazlum conclut » → M, G, M : the last one hands over.
    return [s for i, s in enumerate(order) if i == 0 or s != order[i - 1]]


def relay(cue_lines: list[str], opener: str) -> tuple[str, str]:
    """(who says it, the hand-over sentence) from the « ↪ » line, if any."""
    for line in cue_lines:
        if line.startswith("↪"):
            text = line.removeprefix("↪").strip()
            match = re.match(r"(Mazlum|Guillaume)\s*:?\s*(.*)", text)
            if match:
                return match.group(1)[0], match.group(2)
            return opener, text
    return "", ""


def chip(code: str) -> str:
    name, color = WHO[code]
    return f'<span class="chip" style="background:{color}">{name}</span>'


def rows() -> str:
    out = []
    slides = slides_content.SLIDES
    for i, data in enumerate(slides, 1):
        title = data["title"].replace("\n", " ")
        cue = slides_content.CUES.get(data["title"], "").split("\n")
        who = speakers(cue[0])
        sayer, sentence = relay(cue, who[0] if who else "")
        nxt = slides[i]["title"] if i < len(slides) else None
        next_who = speakers(slides_content.CUES.get(nxt, "🎤").split("\n")[0]) if nxt else []
        ping_pong = cue[0].removeprefix("🎤").strip().lower().startswith(BOTH)
        switch = not ping_pong and bool(next_who) and next_who[0] != (sayer or who[-1])
        who_html = (" ⇄ " if ping_pong else " → ").join(chip(w) for w in who)
        say = f"{chip(sayer)} {html.escape(sentence)}" if sentence else ""
        if switch and not sentence:
            say = f'<span class="warn">sans phrase : {WHO[next_who[0]][0]} enchaîne</span>'
        cls = ' class="handoff"' if (sentence or switch) else ""
        out.append(f"<tr{cls}><td class=n>{i}</td><td>{html.escape(title)}</td>"
                   f"<td class=who>{who_html}</td><td>{say}</td></tr>")
    return "\n".join(out)


PAGE = """<!doctype html><html lang="fr"><head><meta charset="utf-8">
<title>Antisèche des relais</title><style>
@page {{ size: A4 landscape; margin: 8mm; }}
* {{ box-sizing: border-box; }}
body {{ font: 8.2pt "Avenir Next", system-ui, sans-serif; color: #111; margin: 0; }}
h1 {{ font-size: 13pt; margin: 0 0 1mm; }}
p.sub {{ margin: 0 0 2.5mm; color: #555; }}
table {{ width: 100%; border-collapse: collapse; }}
td {{ padding: 0.55mm 1.6mm; border-bottom: 0.2mm solid #e3e3e3; vertical-align: middle; }}
td.n {{ width: 7mm; color: #888; text-align: right; }}
td.who {{ width: 52mm; white-space: nowrap; }}
tr.handoff td {{ background: #fafafa; }}
.chip {{ color: #fff; border-radius: 1.4mm; padding: 0 1.4mm; font-weight: 600; font-size: 7.6pt; }}
.warn {{ color: #b45309; font-style: italic; }}
</style></head><body>
<h1>Antisèche des relais</h1>
<p class="sub">Qui ouvre chaque slide, et la phrase qui passe la main.
→ relais pendant la slide · ⇄ ping-pong. Généré depuis les repères de scène du deck.</p>
<table>{rows}</table></body></html>"""


def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    page = OUT.with_suffix(".html")
    page.write_text(PAGE.format(rows=rows()))
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                    f"--print-to-pdf={OUT.with_suffix('.pdf')}", page.as_uri()],
                   check=True, capture_output=True)
    print(f"OK → {OUT.with_suffix('.pdf')}")


if __name__ == "__main__":
    main()
