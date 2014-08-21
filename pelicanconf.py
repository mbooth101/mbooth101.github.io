# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Mat Booth'
SITENAME = u'Mat\'s Blog-O-Matic'
SITESUBTITLE = u'A Linux and coding blog.'
SITEURL = ''
RELATIVE_URLS = True

TIMEZONE = 'Europe/London'
DEFAULT_LANG = u'en'

THEME = './theme'

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/category-%s.atom.xml'
TAG_FEED_ATOM = 'feeds/tag-%s.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None

# Blogroll
#LINKS =  (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

SOCIAL = (('github', 'https://github.com/mbooth101'),
          ('twitter', 'https://twitter.com/_mbooth'),)

DEFAULT_PAGINATION = False

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

DISQUS_SITENAME = 'mats-blog-o-matic'
TWITTER_USERNAME = '_mbooth'
