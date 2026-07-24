import re
from pathlib import Path

def analyze_frame_range(
    directory: str,
    pattern: str,
    expected_first: int,
    expected_last: int,
) -> dict:
    dir_path = Path(directory)

    # Patrón como regex: imagen.%04d.exr -> imagen\.\d{4}\.exr
    regex = re.compile(
        pattern.replace("%04d", r"(\d{4})")
               .replace("%03d", r"(\d{3})")
    )

    found_frames = []
    for f in sorted(dir_path.iterdir()):
        m = regex.match(f.name)
        if m:
            found_frames.append(int(m.group(1)))

    expected = set(range(expected_first, expected_last + 1))
    found = set(found_frames)

    missing = sorted(expected - found)
    extra = sorted(found - expected)
    duplicates = [
        f for f in found_frames
        if found_frames.count(f) > 1
    ]

    return {
        "found_count": len(found_frames),
        "expected_count": expected_last - expected_first + 1,
        "missing": missing,
        "extra": extra,
        "duplicates": list(set(duplicates)),
        "complete": len(missing) == 0 and len(extra) == 0,
    }
