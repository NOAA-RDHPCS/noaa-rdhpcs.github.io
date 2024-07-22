# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import datetime as dt

project = "NOAA RDHPCS User Documentation"
copyright = (
    "%s, National Oceanic and Atmospheric Administration" % dt.datetime.now().year
)
author = "NOAA RDHPCS"
html_logo = "images/NOAA_RDHPCS.png"
html_favicon = "images/favicon.ico"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx_rtd_theme",
              "sphinx_design",
              "sphinxcontrib.mermaid",
              "sphinx_sitemap"]

templates_path = ["_templates"]
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_baseurl = "https://docs.rdhpcs.noaa.gov"

html_static_path = ["_static"]

html_extra_path = ["_search/google64634d0922861b1a.html",
                   "_search/robots.txt"]

html_css_files = [
    "css/theme_overrides.css",
]

html_sidebars = {
    '**': ['searchbox.html']
}

html_js_files = [
    "js/custom.js",
]

html_context = {
    "vcs_pageview_mode": "edit",
    "display_github": True,
    "github_user": "NOAA-RDHPCS",  # Username
    "github_repo": "noaa-rdhpcs.github.io",  # Repo name
    "github_version": "main",  # Version
    "conf_py_path": "/source/",  # Path in the checkout to the docs root
    "gsce_id": "", # GSCE ID number.  Manage at https://programmablesearchengine.google.com
}

# see https://sphinx-rtd-theme.readthedocs.io/en/stable/configuring.html
html_theme_options = {
    "collapse_navigation": False,
    "sticky_navigation": True,
    "navigation_depth": 4,
    "style_external_links": True,
    "style_nav_header_background": "#efefef",
    "logo_only": True,
}

linkcheck_allowed_redirects = {
    r'http://.*': r'https://.*',
    r'https://.*?\.rdhpcs\.noaa\.gov/?.*': r'https://sso\.noaa\.gov:443/.*',
    r'https://calendar\.google\.com/.*': r'https://workspace\.google\.com/.*',
    r'https://.*?\.google\.com/?.*': r'https://accounts\.google\.com/.*?/signin/.*',
    r'https://.*\.google\.com/?.*': r'https://.*?\.google\.com/?.*?/edit',
    r'https://github\.com/?.*': r'https://github\.com/login',
}

linkcheck_ignore = [
    r'https://noaastore\.blob\.core\.windows\.net/?.*',
    r'https://www\.intel\.com/content/.*',
    r'https://www\.lustre\.org/documentation/',
    r'https://www\.putty\.org/*',
]

# This is needed for backwards compatibility.  We have
# several links that point to pages that require a user
# to authenticate.  This ensures the links pass the check.
linkcheck_allow_unauthorized = True
