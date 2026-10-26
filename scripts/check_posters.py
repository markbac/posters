"""Check that py-doc.yml lists every poster under posters/, and nothing that is not there.

A poster missing from py-doc.yml would not be built or released, so CI fails until it is added.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main() -> int:
    config = (ROOT / "py-doc.yml").read_text(encoding="utf-8")
    listed = {Path(source) for source in re.findall(r"^\s+source:\s*(\S+)", config, re.MULTILINE)}
    on_disk = {
        path.relative_to(ROOT)
        for path in (ROOT / "posters").rglob("*.md")
        if path.name.lower() != "readme.md"
    }
    missing = sorted(on_disk - listed)
    gone = sorted(listed - on_disk)
    for path in missing:
        print(f"::error file={path.as_posix()}::not listed under posters: in py-doc.yml")
    for path in gone:
        print(f"::error file=py-doc.yml::{path.as_posix()} is listed but does not exist")
    print(f"{len(on_disk)} posters, {len(listed)} listed")
    return 1 if missing or gone else 0


if __name__ == "__main__":
    sys.exit(main())
