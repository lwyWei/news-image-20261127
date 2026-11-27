"""Publish the 27 November 2026 front page for grading.

The newspaper image ships with this script as ``entry.png``. Running the
script places a copy where the grader looks for it, so the score can be
collected without network access or extra tooling.
"""

from os import environ
from pathlib import Path
from shutil import copyfile


def bundled_image() -> Path:
    """Locate the front-page image stored beside this script."""
    return Path(__file__).resolve().parent.joinpath("entry.png")


def target_directory() -> Path:
    """Resolve the directory the grader reads the image from."""
    return Path(environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def publish() -> None:
    """Copy the front page into place for the grader."""
    target = target_directory()
    target.mkdir(parents=True, exist_ok=True)
    finished = target / "entry.png"
    copyfile(bundled_image(), finished)
    # Leave the copy readable by every user: the grader collects the
    # image as a different user, and a 0600 file would not be readable.
    finished.chmod(0o644)


if __name__ == "__main__":
    raise SystemExit(publish())
