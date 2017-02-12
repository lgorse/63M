#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Laurent Gorse'
SITENAME = '63 Million'
SITEURL = 'https://lgorse.github.io/63M/'

PATH = 'content'
IGNORE_FILES = ['.ipynb-checkpoints', '*/.ipynb-checkpoints/*.ipynb']

TIMEZONE = 'PST8PDT'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/laurent79'),
          ('linkedin','https://www.linkedin.com/in/laurent-gorse-373b5414'),
          ('github', 'https://github.com/lgorse/why-trump/'),
          ('facebook','https://www.facebook.com/laurent.gorse.73'))

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

MARKUP = ('md', 'ipynb')

PLUGIN_PATH = './plugins'
PLUGINS = ['ipynb.markup']

THEME = 'output/theme'
