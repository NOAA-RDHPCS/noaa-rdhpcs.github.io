# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import datetime as dt

project = 'NOAA RDHPCS User Documentation'
copyright = '%s, NOAA' % dt.datetime.now().year
author = 'NOAA RDHPCS'
html_logo = 'images/NOAA_RDHPCS.png'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_rtd_theme'
]

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

html_context = {
    'vcs_pageview_mode': 'edit',
    'display_github': False,
    'github_user': 'NOAA-GFDL',  # Username
    'github_repo': 'rdhpcs-user-docs',  # Repo name
    'github_version': 'master',  # Version
    'conf_py_path': '/',  # Path in the checkout to the docs root
}

# see https://sphinx-rtd-theme.readthedocs.io/en/stable/configuring.html
html_theme_options = {
    'canonical_url': 'https://docs.rdhpcs.noaa.gov',
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'style_external_links': True,
    'style_nav_header_background': '#efefef',
    'logo_only': True,
}
