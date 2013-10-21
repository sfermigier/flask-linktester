# -*- coding: utf-8 -*-

import sys, os

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath('_themes'))

# Reused
from version import VERSION
NAME = "Flask-LinkTester"
YEAR = "2012-2013"
AUTHOR = "Stefane Fermigier"


# -- General configuration -----------------------------------------------------

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.intersphinx']
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

project = unicode(NAME)
copyright = u"%s, %s" % (YEAR, AUTHOR)

version = VERSION
release = VERSION

exclude_patterns = ['_build']

html_theme = 'flask_small'
html_theme_path = ['_themes']
html_static_path = ['_static']
html_theme_options = {
     #'index_logo': 'flask-testing.png', # TODO
     'github_fork': 'sfermigier/flask-linktester'
}

htmlhelp_basename = 'flask-linktesterdoc'

# -- Options for LaTeX output --------------------------------------------------

# The paper size ('letter' or 'a4').
latex_paper_size = 'a4'

# The font size ('10pt', '11pt' or '12pt').
#latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('index', '%s.tex' % NAME.lower(), u'%s Documentation' % NAME,
   AUTHOR, 'manual'),
]

# -- Options for manual page output --------------------------------------------

man_pages = [
    ('index', str(NAME.lower()), u'%s Documentation' % NAME, [AUTHOR], 1)
]
