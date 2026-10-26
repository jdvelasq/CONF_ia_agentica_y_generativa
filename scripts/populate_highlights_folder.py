"""Copy the introductory highlights from agentic-playground Markdown files."""

import re
from pathlib import Path

SOURCE_DIR = Path("/Volumes/GitHub/agentic-playground")
HIGHLIGHTS_DIR = Path(__file__).resolve().parent.parent / "highlights"
HEADING_PATTERN = re.compile(r"^[ \t]*#{1,6}[ \t]+\S")


def extract_highlights(markdown: str, source_name: str) -> str:
    """Return the first heading and its introductory content before the next heading."""
    lines = markdown.splitlines()
    title_index = next(
        (index for index, line in enumerate(lines) if HEADING_PATTERN.match(line)),
        None,
    )
    if title_index is None:
        raise ValueError(f"{source_name} does not contain a Markdown title")

    next_section_index = next(
        (
            index
            for index in range(title_index + 1, len(lines))
            if HEADING_PATTERN.match(lines[index])
        ),
        len(lines),
    )
    highlights = "\n".join(lines[title_index:next_section_index]).rstrip()
    return f"{highlights}\n"


def main() -> None:
    if not SOURCE_DIR.is_dir():
        raise FileNotFoundError(f"Source directory does not exist: {SOURCE_DIR}")

    source_files = sorted(SOURCE_DIR.glob("*.md"))
    if not source_files:
        raise FileNotFoundError(f"No Markdown files found in {SOURCE_DIR}")

    HIGHLIGHTS_DIR.mkdir(parents=True, exist_ok=True)
    for source_file in source_files:
        content = source_file.read_text(encoding="utf-8")
        highlights = extract_highlights(content, source_file.name)
        (HIGHLIGHTS_DIR / source_file.name).write_text(
            highlights,
            encoding="utf-8",
        )

    print(
        f"Created highlights for {len(source_files)} Markdown files in {HIGHLIGHTS_DIR}"
    )


if __name__ == "__main__":
    main()
