from pathlib import Path
import sys

def resource_path(relative_path: str) -> Path:
    if getattr(sys, "frozen", False):
        # Nuitka
        base_path = Path(sys.argv[0]).resolve().parent
    else:
        # Normal Python run
        base_path = Path(__file__).resolve().parent.parent

    return base_path / relative_path