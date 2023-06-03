AUTHOR = "Mat Booth"
SITENAME = "Mat's Blog-O-Matic"
SITESUBTITLE = "A Linux, coding and DIY blog."
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TAG_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'https://getpelican.com/'),
#         ('Python.org', 'https://www.python.org/'),
#         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('github', 'https://github.com/mbooth101'),
          ('twitter', 'https://twitter.com/FOSS_mbooth'),
          ('email', 'mailto:blog@matbooth.co.uk'),)

# Article list pagination
DEFAULT_PAGINATION = 25

# Site menu entries
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = [('Fedora', '/tag/fedora.html'), ('Eclipse', '/tag/eclipse.html'), ('DIY', '/tag/diy.html')]

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
