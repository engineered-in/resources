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
import sphinx_rtd_theme
from pathlib import Path
from os import path, getenv
import toml

_versions = toml.load(Path(__file__).parent / "version.toml")

# -- Project information -----------------------------------------------------

project = 'Python DevEnv Setup Guide'
copyright = '2024, engineered.co.in'
author = 'Priya'

# The full version, including alpha/beta/rc tags
release = f"Release {_versions.get('version', '0.1')}"
version = f"Version {_versions.get('version', '0.1')}"

latex_elements = {
  'papersize': 'a4paper',
  'pointsize': '12pt',
  'preamble': '',
  'figure_align': 'htbp'
}

latex_documents = [
  ('index', f'python-devenv-setup-guide.tex', 'Python DevEnv Setup Guide',
   'Priya', 'manual'),
]


highlight_language = 'powershell'

html_context = {
    "display_gitlab": True,
    "gitlab_host": "gitlab.com",
    "gitlab_user": getenv("CI_PROJECT_NAMESPACE"),
    "gitlab_repo": getenv("CI_PROJECT_NAME"),
    "gitlab_version": getenv("CI_DEFAULT_BRANCH"),
    "conf_py_path": "/docs/",
    "source_suffix": ".rst",
    "external_links": [
        ("GitLab Repository", getenv("CI_PROJECT_URL")),
        ("Development Best Practices Wiki", "https://gitlab.com/engineered-in/resources/-/wikis/home"),
    ]
}

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.intersphinx', 'sphinx_rtd_theme', 'sphinx.ext.napoleon', 'sphinx_copybutton'
]

intersphinx_mapping = {'python': ('https://docs.python.org/3', None),
'pandas': ('https://pandas.pydata.org/docs/', None),
}

autodoc_default_options = {
    'member-order': 'bysource',
    'special-members': '__init__',
    'undoc-members': True,
    'exclude-members': '__weakref__'
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    'collapse_navigation': False,  # Keeps the navigation menu open
    'sticky_navigation': True,     # Sticky navigation menu
    'navigation_depth': 3,         # Depth of the table of contents
}


# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = 'Python DevEnv Setup Guide'

# A shorter title for the navigation bar.  Default is the same as html_title.
html_short_title = 'Python DevEnv Setup Guide'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'

html_show_sourcelink = True
html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = True

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = './_static/icons/EngineeredIn-logo.svg'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = './_static/icons/favicon.ico'
