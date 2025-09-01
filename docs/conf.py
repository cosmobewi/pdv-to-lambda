# docs/conf.py
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).resolve().parent / "cosmobewi-shared"))

from conf_shared import *     # shared theme & config
include_local_paths(__file__) # enable local overrides

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
BASE_PDV = Path(__file__).resolve().parent
bibtex_bibfiles = [str(BASE_PDV / 'refs.bib')]

exclude_patterns = []