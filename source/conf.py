# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'NietteTTS'
copyright = '2024-%Y, Pallas da Silva Guedes'
author = 'Pallas da Silva Guedes'
release = '1.0.4-alpha'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser', 'sphinx_togglebutton']
templates_path = ['_templates']
exclude_patterns = []
source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}
language = 'pt-BR'

html_theme_options = {
	"repository_url": "https://github.com/NietteLabs/niettelabs.github.io",
	"use_repository_button": True,
	"announcement": "Essa é uma documentação está em estagio alpha! Sofrerar alterações conforme o tempo.",
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
html_static_path = ['_static']
html_show_sphinx = True
html_logo = '../imgs/NietteTTS.png'
html_favicon = '../imgs/NietteTTS.png'
