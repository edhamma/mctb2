# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Mastering the Core Teachings of the Buddha'
copyright = 'Digital'
author = 'The Arahant Daniel M. Ingram'

import git, urllib.parse
mctb2Commit=(head:=git.Repo(search_parent_directories=True).head).object.hexsha[:7]

release = mctb2Commit
version = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.todo']
todo_include_todos=True

templates_path = ['_templates']
exclude_patterns = []


html_theme_options = {
    'github_user':'eudoxos',
    'github_repo':'mctb2',
    'github_banner':'true',
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']


epub_title = project
epub_author = author
epub_publisher = '~~ eudoxos.github.io/mctb2 WIP ~~'
epub_copyright = copyright
epub_cover = ('_static/cover.jpg','epub-cover.html')
epub_language='en'
epub_basename='mctb2'
epub_use_index=False
epub_scheme='ISBN'
epub_identifier = '978-1-91159-710-0'
# A unique identification for the text.
epub_uid = 'mastering-the-core-teachings-of-the-buddha-2'

