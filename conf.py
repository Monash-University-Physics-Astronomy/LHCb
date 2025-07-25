# Configuration file for the Sphinx documentation builder.
# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here.
import sys
import os
sys.path.insert(0, os.path.abspath("."))

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

