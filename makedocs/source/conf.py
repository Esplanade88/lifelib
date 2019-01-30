#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# lifelib documentation build configuration file, created by
# sphinx-quickstart on Sat Nov 11 16:48:39 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

here = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, os.path.abspath(here + "../.."))

# Insert project path in sys.path so that each directory under
# the path is interpreted as the top level package in the API reference.
sys.path.insert(0, os.path.abspath(here + "/../../lifelib/projects"))
sys.path.insert(0, '')  # Add the current folder at front.

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'nbsphinx',
    'sphinx_gallery.gen_gallery',
    'sphinxcontrib.blockdiag']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'lifelib'
copyright = '2017-2019, Fumito Hamamura'
author = 'Fumito Hamamura'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
import lifelib
version = lifelib.__version__
# The full version, including alpha/beta/rc tags.
release = lifelib.__version__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', '**.ipynb_checkpoints']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# import sphinx_rtd_theme
# html_theme = 'sphinx_rtd_theme'
# html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
import sphinx_bootstrap_theme
html_theme = 'bootstrap'
html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#

# See below for options of bootstrap theme
# https://ryan-roemer.github.io/sphinx-bootstrap-theme/README.html
html_theme_options = {

    'bootstrap_version': "3",

    # Tab name for entire site. (Default: "Site")
    'navbar_site_name': "Menu",

    # A list of tuples containing pages or urls to link to.
    # Valid tuples should be in the following forms:
    #    (name, page)                 # a link to a page
    #    (name, "/aa/bb", 1)          # a link to an arbitrary relative url
    #    (name, "http://example.com", True) # arbitrary absolute url
    # Note the "1" or "True" value above as the third argument to indicate
    # an arbitrary url.
    'navbar_links': [
        # ("Quick Start", "quickstart"),
        ("Projects", "projects/index"),
        ("Gallery", "generated_examples/index")
    ],

    # Render the next and previous page links in navbar. (Default: true)
    'navbar_sidebarrel': False,

    # Render the current pages TOC in the navbar. (Default: true)
    'navbar_pagenav': True,

    # Tab name for the current pages TOC. (Default: "Page")
    'navbar_pagenav_name': "Contents",

    # Global TOC depth for "site" navbar tab. (Default: 1)
    # Switching to -1 shows all levels.
    'globaltoc_depth': 2,

    # Location of link to source.
    # Options are "nav" (default), "footer" or anything else to exclude.
    'source_link_position': "hide",

    # HTML navbar class (Default: "navbar") to attach to <div> element.
    # For black navbar, do "navbar navbar-inverse"
    'navbar_class': "navbar navbar-inverse",

    # Bootswatch (http://bootswatch.com/) theme.
    #
    # Options are nothing (default) or the name of a valid theme
    # such as "cosmo" or "sandstone".
    #
    # The set of valid themes depend on the version of Bootstrap
    # that's used (the next config option).
    #
    # Currently, the supported themes are:
    # - Bootstrap 2: https://bootswatch.com/2
    # - Bootstrap 3: https://bootswatch.com/3
    'bootswatch_theme': "cosmo",

}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}
html_sidebars = {'index': None,
                 '*': ['globaltoc_sidebar.html'],
                 'projects/**': ['globaltoc_sidebar.html'],
                 'generated_examples/**': None}

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'lifelibdoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'lifelib.tex', 'lifelib Documentation',
     'Fumito Hamamura', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'lifelib', 'lifelib Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'lifelib', 'lifelib Documentation',
     author, 'lifelib', 'One line description of project.',
     'Miscellaneous'),
]


# -- Options for Auto summary -------------------------------------------
autosummary_generate = True
# autoclass_content = 'class'
autodoc_default_flags = [
    'members', 'inherited_members',  # 'undoc-members',
    'show-inheritance']
    # , 'private-members', 'special-members']
autodoc_member_order = 'bysource'


# -- Options for Gallery -------------------------------------------
from sphinx_gallery.sorting import ExplicitOrder
sphinx_gallery_conf = {
    # path to your examples scripts
    'ignore_pattern': '^(?!.*plot_)',
    'examples_dirs': '../../lifelib/projects',
    'subsection_order': ExplicitOrder(
        ['../../lifelib/projects/simplelife',
         '../../lifelib/projects/nestedlife',
         '../../lifelib/projects/ifrs17sim']),
    # path where to save gallery generated examples
    'gallery_dirs': 'generated_examples',
    # Suppress warning:
    'backreferences_dir': False,
    'download_all_examples': False,
    'download_section_examples': False
}


# blockdiag_fontpath = 'c:/windows/fonts/calibri.ttf'
blockdiag_html_image_format = 'SVG'

# Hide download note and buttons from gallery pages.
# https://github.com/ryan-roemer/sphinx-bootstrap-theme
def setup(app):
    app.add_stylesheet("custom-style.css")
