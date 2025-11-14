# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------

# Add custom module paths if needed
# sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'UHC Member Account Setup'
copyright = '2025'
author = 'UHC Support Guide Team'

# Full version number
release = '1.0.0'

# -- General configuration ---------------------------------------------------

# Sphinx extensions (add more if needed)
extensions = []

# Allow raw HTML inside .rst files
raw_enabled = True
html_allow_unsafe = True

# Templates & files to ignore
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# HTML theme (add your theme if using one)
# html_theme = 'sphinx_rtd_theme'

# Page Titles
html_title = "How to Create a UHC Member Account – Step-by-Step Guide"
html_short_title = "UHC Account Setup"

# Optional favicon
html_favicon = 'favicon.ico'  # Add your favicon file in root or _static folder

# Hide "View Page Source"
html_show_sourcelink = False

# Theme customizations
html_theme_options = {
    'show_powered_by': False,
}

# Static assets
# html_static_path = ['_static']
