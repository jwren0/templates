import os
import sys

sys.path.insert(0, os.path.abspath(
    os.path.join("..", "..", "src")
))

project = "example"
release = "0.0.1"
author = "jwren0"
copyright = "2023, jwren0"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.intersphinx",
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}

html_theme = "furo"
