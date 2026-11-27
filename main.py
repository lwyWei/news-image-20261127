"""Copy the 27 November 2026 front page to the grading directory.

The image ``entry.png`` travels with this script. This program places a
copy where the grader expects it, using only the Python standard library,
so the entry needs no network access and no extra packages.
"""

import os
import shutil


IMAGE_NAME = "entry.png"
DEFAULT_OUTPUT = "/output"


def image_path():
    """Return the path of the image shipped beside this script."""
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, IMAGE_NAME)


def output_dir():
    """Return the directory the grader reads, honouring the environment."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT)


def main():
    """Copy the front page into the output directory."""
    destination = output_dir()
    os.makedirs(destination, exist_ok=True)
    target = os.path.join(destination, IMAGE_NAME)
    shutil.copyfile(image_path(), target)
    # Make the copy world-readable: the grader collects it as another user.
    os.chmod(target, 0o644)
    return 0


main()
