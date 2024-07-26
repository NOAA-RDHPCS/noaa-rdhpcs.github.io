# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import datetime as dt

# Sphinx Configuration Items
project = "NOAA RDHPCS User Documentation"
copyright = (
    f"{dt.datetime.now().year}, National Oceanic and Atmospheric Administration"
)
author = "NOAA RDHPCS"

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
html_title = "NOAA RDHPCS"
html_logo = "images/NOAA_RDHPCS.png"
html_favicon = "images/favicon.ico"
html_show_copyright = False
html_theme = "sphinx_rtd_theme"
html_baseurl = "https://docs.rdhpcs.noaa.gov/"

html_static_path = ["_static"]
html_extra_path = ["_search/google64634d0922861b1a.html",
                   "_search/robots.txt"]

html_css_files = [
    "css/theme_overrides.css",
]

html_context = {
    "display_github": True,
    "github_user": "NOAA-RDHPCS",  # Username
    "github_repo": "noaa-rdhpcs.github.io",  # Repo name
    "github_version": "main",  # Version
    "conf_py_path": "/source/",  # Path in the checkout to the docs root
    "version": "<a href='/help/'>Need Help? Click Here</a>",
    "project_home_url": "https://www.noaa.gov/information-technology/hpcc", # URL to the Project Home page
    "project_home_name": False, # False, or string with the Project name (e.g., NOAA RDHPCS Home)
    "github_issue_button": True, # Display the Open issue on GitHub button
    "show_sphinx": False,
}

# see https://sphinx-rtd-theme.readthedocs.io/en/stable/configuring.html
html_theme_options = {
    "collapse_navigation": False,
    "sticky_navigation": True,
    "navigation_depth": 4,
    "style_external_links": True,
    "style_nav_header_background": "#efefef",
    "logo_only": True,
    "display_version": True,
    "vcs_pageview_mode": "blob",

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

# Additional sitemap settings
# https://sphinx-sitemap.readthedocs.io/en/latest/index.html
sitemap_url_scheme = "{link}"
sitemap_locales = [None]
sitemap_excludes = [
    "search.html",
    "genindex.html",
]
