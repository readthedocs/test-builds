import os

AUTHOR = '@humitos'
SITENAME = 'test-builds'

READTHEDOCS_PROJECT = os.environ.get('READTHEDOCS_PROJECT')
READTHEDOCS_VERSION = os.environ.get('READTHEDOCS_VERSION')
READTHEDOCS_LANGUAGE = os.environ.get('READTHEDOCS_LANGUAGE')

# Define SITEURL properly to be hosted on Read the Docs on a path different than /
# allowing mutliple versions.
SITEURL = f'https://{READTHEDOCS_PROJECT}.readthedocs.io/{READTHEDOCS_LANGUAGE}/{READTHEDOCS_VERSION}'

PATH = '.'

TIMEZONE = 'Europe/Rome'
DEFAULT_LANG = 'en'
OUTPUT_PATH = 'output/'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
