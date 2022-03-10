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
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
import sphinx_material


# -- Project information -----------------------------------------------------

project = 'What is RDF and what is it good for?'
copyright = '2022, Joshua Tauberer'
author = 'Joshua Tauberer'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx_material']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

# Required theme setup
html_theme = 'sphinx_material'
# Set link name generated in the top bar.
html_title = 'Resource Description Framework'
# Material theme options (see theme.conf for more information)
html_theme_options = {
    # 'base_url': 'https://docs.chipsee.com',
    # Set the color and the accent color
    'color_primary': 'blue',
    'color_accent': 'blue',
    'globaltoc_depth': 1,
    'globaltoc_collapse': True,
    'globaltoc_includehidden': True,
    'html_minify': True,
    'css_minify': True,
 }
html_sidebars = {
    "**": ["localtoc.html", "searchbox.html"]
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = ['css/custom.css']

html_show_sourcelink = False
