import os

# Default settings
project = 'Test Builds'
extensions = [
    'sphinx_autorun',
]

# Include all your settings here
html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    'enable_search_shortcuts': False,
}

template_path = [
    "templates",
]

# We need to tell to our builder that we are building on Read the Docs
# Ideally, the theme should get this automatically from the environment
# instead of forcing us to define it on its context
#
# Note that Read the Docs is passing a lot of context here:
# https://github.com/readthedocs/readthedocs.org/blob/e18b40f6fe7c2c058bbf681063c1c577b5e8e9d3/readthedocs/doc_builder/templates/doc_builder/conf.py.tmpl#L99-L149
# We would need to audit all of it, remove the ones that are not required,
# and adapt our Sphinx theme to use environment variables --which will be the
# official way to communicate with all the builders
#
# For now, I'm only defining the variables I need to build the `versions.html` from the theme
# https://github.com/readthedocs/sphinx_rtd_theme/blob/9d88b9e4e1e17896c6231358a89da4612ff7bc90/sphinx_rtd_theme/versions.html#L1
# Note that everything from inside "rst-other-versions" is gonna be replaced by the `/footer_html/` response,
# so they are not needed to be defined.
# if "READTHEDOCS" in os.environ:
#     html_context = {
#         "READTHEDOCS": True,
#         "current_version": os.environ.get('READTHEDOCS_VERSION'),
#     }
