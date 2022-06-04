# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import re
import sys


# -- Project information -----------------------------------------------------

project: str = "Test"
copyright: str = "Present, Alex Nørgaard"
author: str = "Alex Nørgaard"

version = "1.0"
release = version

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
sys.path.insert(0, os.path.abspath(".."))

extensions: list[str] = [
    "sphinx.ext.autodoc",
]

autodoc_typehints: str = "both"
autodoc_typehints_format: str = "short"
autodoc_typehints_description_target: str = "documented"
autodoc_member_order: str = "bysource"
autodoc_preserve_defaults: bool = False
autodoc_type_aliases: dict[str, str] = {
    "PathLike": "os.PathLike",
}

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns: list[str] = ["build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme: str = "furo"

