# Configuration file for the Sphinx documentation builder.
# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here.
import sys
import os
sys.path.insert(0, os.path.abspath("."))
from inspect import getsourcefile

#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Monash LHCb'
copyright = '2025, Monash LHCb'
author = 'Monash LHCb'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


extensions = ['sphinx.ext.duration',
              'sphinx.ext.doctest',
              'sphinx.ext.autodoc',
              'sphinx.ext.autosummary',
              'myst_parser',
              'nbsphinx',
]

myst_enable_extensions = ["dollarmath"]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
# html_theme = 'furo'
html_theme = 'sphinx_rtd_theme'


html_static_path = ['_static']

# EPUB options
epub_show_urls = 'footnote'


# Get path to directory containing this file, conf.py.
DOCS_DIRECTORY = os.path.dirname(os.path.abspath(getsourcefile(lambda: 0)))

def ensure_pandoc_installed(_):
    import pypandoc

    # Download pandoc if necessary. If pandoc is already installed and on
    # the PATH, the installed version will be used. Otherwise, we will
    # download a copy of pandoc into docs/bin/ and add that to our PATH.
    pandoc_dir = os.path.join(DOCS_DIRECTORY, "bin")
    # Add dir containing pandoc binary to the PATH environment variable
    if pandoc_dir not in os.environ["PATH"].split(os.pathsep):
        os.environ["PATH"] += os.pathsep + pandoc_dir
    pypandoc.ensure_pandoc_installed(
        # quiet=True,
        targetfolder=pandoc_dir,
        delete_installer=True,
    )


def setup(app):
    app.connect("builder-inited", ensure_pandoc_installed)
