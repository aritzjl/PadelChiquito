
import os
import sys
import django
# Obtén la ruta absoluta del directorio raíz de tu proyecto
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Agrega el directorio que contiene tu proyecto Django a sys.path
sys.path.insert(0, project_root)

# Establece el valor correcto para DJANGO_SETTINGS_MODULE
os.environ['DJANGO_SETTINGS_MODULE'] = 'padelchiquito.settings'

# Inicializa Django
django.setup()()


# Resto del código...
copyright = '2024, TenBeltz'
author = 'TenBeltz'
release = 'v10.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary', 
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode'
]

templates_path = ['_templates']
exclude_patterns = []

language = 'es'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
