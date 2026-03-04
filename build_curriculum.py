from __future__ import annotations

import json
import re
from dataclasses import dataclass
from html import escape
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).parent
CURRICULUM_DIR = ROOT / "curriculum"
OUTPUT_DIR = ROOT / "built" / "weeks"
MANIFEST_PATH = ROOT / "built" / "manifest.json"
WEEK_PATTERN = re.compile(r"week(\d{2})\.md$")


@dataclass
class Heading:
    level: int
    text: str
    slug: str


def slugify(text: str) -> str:
    core = re.sub(r"<[^>]+>", "", text)
    core = re.sub(r"[^\w\s\-가-힣]", "", core, flags=re.UNICODE).strip().lower()
    core = re.sub(r"[\s_]+", "-", core)
    return core or "section"


def inline_markdown(text: str) -> str:
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", text)
    return text


def normalize_mermaid(content: str) -> str:
    def repl(match: re.Match[str]) -> str:
        return "[" + match.group(1).replace("\n", "<br/>") + "]"

    normalized = re.sub(r"\[(.*?)\]", repl, content, flags=re.DOTALL)

    lines = [line.rstrip() for line in normalized.splitlines() if line.strip()]
    if not lines:
        return ""

    first = lines[0].strip()
    m = re.match(r"^(flowchart|graph)\s+([A-Za-z]{2})$", first)
    if m:
        lines[0] = f"{m.group(1)} {m.group(2)};"

    body = []
    for idx, line in enumerate(lines):
        text = line.strip()
        if idx == 0:
            body.append(text)
            continue
        if not text.endswith(';'):
            text += ';'
        body.append(text)

    return "\n".join(body)


def convert_markdown(md: str) -> tuple[str, list[Heading], str]:
    lines = md.replace("\r\n", "\n").split("\n")
    html: list[str] = []
    headings: list[Heading] = []
    slug_seen: dict[str, int] = {}

    in_code = False
    code_lang = ""
    code_buffer: list[str] = []
    in_ul = False
    in_ol = False
    in_table = False

    i = 0
    while i < len(lines):
        raw = lines[i]
        line = raw.strip()

        if line.startswith("```"):
            if not in_code:
                in_code = True
                code_lang = line[3:].strip().lower()
                code_buffer = []
            else:
                content = "\n".join(code_buffer)
                if code_lang == "mermaid":
                    html.append(f'<div class="mermaid">{normalize_mermaid(content)}</div>')
                else:
                    klass = f' class="language-{code_lang}"' if code_lang else ""
                    html.append(f"<pre><code{klass}>{escape(content)}</code></pre>")
                in_code = False
                code_lang = ""
                code_buffer = []
            i += 1
            continue

        if in_code:
            code_buffer.append(raw)
            i += 1
            continue

        if not line:
            if in_ul:
                html.append("</ul>")
                in_ul = False
            if in_ol:
                html.append("</ol>")
                in_ol = False
            if in_table:
                html.append("</tbody></table>")
                in_table = False
            i += 1
            continue

        # GitHub callout style: > [!NOTE]
        if line.startswith("> [!"):
            callout_lines: list[str] = []
            callout_type = line[4:].split("]", 1)[0].lower()
            i += 1
            while i < len(lines) and lines[i].strip().startswith(">"):
                callout_lines.append(lines[i].strip()[1:].strip())
                i += 1
            body = " ".join(callout_lines).strip()
            html.append(
                f'<div class="callout callout-{escape(callout_type)}">'
                f'<div class="callout-title">{escape(callout_type.upper())}</div>'
                f"<p>{inline_markdown(escape(body))}</p></div>"
            )
            continue

        if line == "---":
            html.append("<hr />")
            i += 1
            continue

        heading = re.match(r"^(#{1,6})\s+(.*)$", line)
        if heading:
            if in_ul:
                html.append("</ul>")
                in_ul = False
            if in_ol:
                html.append("</ol>")
                in_ol = False
            if in_table:
                html.append("</tbody></table>")
                in_table = False

            level = len(heading.group(1))
            text = inline_markdown(escape(heading.group(2)))
            base_slug = slugify(heading.group(2))
            count = slug_seen.get(base_slug, 0)
            slug_seen[base_slug] = count + 1
            slug = base_slug if count == 0 else f"{base_slug}-{count + 1}"
            headings.append(Heading(level=level, text=heading.group(2), slug=slug))
            html.append(f'<h{level} id="{slug}">{text}</h{level}>')
            i += 1
            continue

        if re.match(r"^\|.+\|$", line):
            cols = [inline_markdown(escape(c.strip())) for c in line.split("|")[1:-1]]
            next_line = lines[i + 1].strip() if i + 1 < len(lines) else ""
            is_separator = bool(re.match(r"^\|?\s*[:-]-+", next_line))

            if not in_table:
                html.append("<table>")
                in_table = True

            if is_separator:
                html.append("<thead><tr>" + "".join(f"<th>{c}</th>" for c in cols) + "</tr></thead><tbody>")
                i += 2
            else:
                html.append("<tr>" + "".join(f"<td>{c}</td>" for c in cols) + "</tr>")
                i += 1
            continue
        elif in_table:
            html.append("</tbody></table>")
            in_table = False

        ul = re.match(r"^[-*]\s+(.*)$", line)
        if ul:
            if not in_ul:
                if in_ol:
                    html.append("</ol>")
                    in_ol = False
                html.append("<ul>")
                in_ul = True
            html.append(f"<li>{inline_markdown(escape(ul.group(1)))}</li>")
            i += 1
            continue

        ol = re.match(r"^\d+\.\s+(.*)$", line)
        if ol:
            if not in_ol:
                if in_ul:
                    html.append("</ul>")
                    in_ul = False
                html.append("<ol>")
                in_ol = True
            html.append(f"<li>{inline_markdown(escape(ol.group(1)))}</li>")
            i += 1
            continue

        if in_ul:
            html.append("</ul>")
            in_ul = False
        if in_ol:
            html.append("</ol>")
            in_ol = False

        if line.startswith(">"):
            text = line[1:].strip()
            html.append(f"<blockquote><p>{inline_markdown(escape(text))}</p></blockquote>")
        else:
            html.append(f"<p>{inline_markdown(escape(line))}</p>")

        i += 1

    if in_ul:
        html.append("</ul>")
    if in_ol:
        html.append("</ol>")
    if in_table:
        html.append("</tbody></table>")

    title = headings[0].text if headings else "Untitled"
    wrapped = '<article class="doc-content">' + "\n".join(html) + "</article>"
    return wrapped, headings, title


def iter_week_files() -> Iterable[Path]:
    candidates = []
    for path in CURRICULUM_DIR.glob("week*.md"):
        match = WEEK_PATTERN.search(path.name)
        if match:
            candidates.append((int(match.group(1)), path))
    for _, path in sorted(candidates):
        yield path


def build() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    lectures: list[dict[str, str | int]] = []

    for idx, md_path in enumerate(iter_week_files(), start=1):
        week = WEEK_PATTERN.search(md_path.name).group(1)
        source = md_path.read_text(encoding="utf-8")
        html, _headings, title = convert_markdown(source)
        out_name = f"week{week}.html"
        out_path = OUTPUT_DIR / out_name
        out_path.write_text(html, encoding="utf-8")
        lectures.append({
            "id": idx - 1,
            "week": week,
            "title": title,
            "source": f"curriculum/{md_path.name}",
            "html": f"built/weeks/{out_name}",
        })

    MANIFEST_PATH.parent.mkdir(parents=True, exist_ok=True)
    MANIFEST_PATH.write_text(
        json.dumps({"total": len(lectures), "lectures": lectures}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"Built {len(lectures)} lecture HTML files into {OUTPUT_DIR}")


if __name__ == "__main__":
    build()
