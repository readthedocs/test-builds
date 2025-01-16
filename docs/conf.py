# Default settings
project = 'Test Builds'
extensions = [
    'sphinx_autorun',
]


# Include all your settings here
html_theme = 'furo'

templates_path = ["_templates"]
html_sidebars = {
    "**": ["sidebar/variant-selector.html"]
}
