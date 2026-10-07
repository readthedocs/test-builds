# -*- coding: utf-8 -*-

# Default settings
project = 'Test Builds'
extensions = [
    # Both generate DOM with JavaScript, see readthedocs/addons#528
    'sphinx_copybutton',
    'sphinx.ext.mathjax',
]

# Hide ">>> " prompts via the copy button, like CPython does
copybutton_prompt_text = '>>> '


# Include all your settings here
html_theme = 'sphinx_rtd_theme'
