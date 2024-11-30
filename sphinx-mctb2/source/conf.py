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

extensions = ['sphinx.ext.todo', 'myst_parser']
myst_enable_extensions=['attrs_inline','linkify','colon_fence','attrs_block', 'deflist']

todo_include_todos=True

templates_path = ['_templates']
exclude_patterns = []


html_theme_options=dict(
    use_download_button=False,
    use_source_button=False,
    repository_provider='github',
    repository_url='https://github.com/edhamma/mctb2',
    use_edit_page_button=True,
    use_repository_button=True,
    use_issues_button=True,
)

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
html_static_path = ['_static']
# html_css_files=[ 'custom.css' ]
html_title = project


epub_title = project
epub_author = author
epub_publisher = '~~ edhamma.github.io/mctb2 WIP ~~'
epub_copyright = copyright
epub_cover = ('_static/cover.jpg','epub-cover.html')
epub_language='en'
epub_basename='mctb2'
epub_use_index=False
epub_scheme='ISBN'
epub_identifier = '978-1-91159-710-0'
# A unique identification for the text.
epub_uid = 'mastering-the-core-teachings-of-the-buddha-2'

