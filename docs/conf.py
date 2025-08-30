from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parent.parent))
from conf_base import * 

# -- Project information -----------------------------------------------------
project = 'Constante cosmologique et dilution des champs sans masse'
author = 'Projet Théorie des Horloges Cosmologiques'
release = '0.1'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.mathjax',
    'sphinx.ext.napoleon',
    'sphinxcontrib.bibtex',
]
bibtex_bibfiles = ['refs.bib']

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
html_theme = 'alabaster'
html_static_path = ['_static']
