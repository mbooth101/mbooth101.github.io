# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Mat Booth'
SITENAME = 'Mat\'s Blog-O-Matic'
SITESUBTITLE = 'A Linux, coding and DIY blog.'
SITEURL = ''
RELATIVE_URLS = True

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/category-%s.atom.xml'
TAG_FEED_ATOM = 'feeds/tag-%s.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (('github', 'https://github.com/mbooth101'),
          ('twitter', 'https://twitter.com/FOSS_mbooth'),
          ('email', 'mailto:mbooth@fedoraproject.org'),)

STATIC_PATHS = ['images']

DEFAULT_PAGINATION = False

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = [('Fedora', '/tag/fedora.html'), ('Eclipse', '/tag/eclipse.html'), ('DIY', '/tag/diy.html')]

#DISQUS_SITENAME = 'mats-blog-o-matic'
TWITTER_USERNAME = 'FOSS_mbooth'
