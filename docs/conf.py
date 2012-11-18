# -*- coding: utf-8 -*-

import sys, os

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.append(os.path.abspath('_themes'))

# -- General configuration -----------------------------------------------------

extensions = ['sphinx.ext.autodoc', 'sphinxcontrib.blockdiag']
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

# General information about the project.
project = u'Acrylamid'
copyright = u'2012, posativ'

version = '0.5'
release = '0.5.0'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

exclude_patterns = ['_build']

html_theme = 'werkzeug'
html_theme_path = ['_themes']
html_static_path = ['_static']

htmlhelp_basename = 'acrylamiddoc'

# -- Options for LaTeX output --------------------------------------------------

latex_documents = [
  ('index', 'acrylamid.tex', u'Acrylamid Documentation',
   u'posativ', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Additional stuff for the LaTeX preamble.
#latex_preamble = ''

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'acrylamid', u'Acrylamid Documentation',
     [u'posativ'], 1)
]
