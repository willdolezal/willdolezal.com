# GENERAL SETTINGS
AUTHOR = 'Will Dolezal'
SITENAME = 'willdolezal.com'
SITEURL = "https://willdolezal.com"
THEME = "themes/pelican-alchemy/alchemy"
PATH = "content"
TIMEZONE = 'America/Vancouver'
BOOTSTRAP_CSS = "https://cdn.jsdelivr.net/npm/bootswatch@v4.3.1/dist/lux/bootstrap.min.css"
DEFAULT_LANG = 'en'
DEFAULT_PAGINATION = False
HIDE_AUTHORS = True

#Shift location of particular files
STATIC_PATHS = ["extra/favicon.ico"]
EXTRA_PATH_METADATA = {
    "extra/favicon.ico": {"path":"favicon.ico"},
}

# Suppress Author(s), Archives and Tag(s) pages
AUTHOR_SAVE_AS = ""
AUTHORS_SAVE_AS = ""
ARCHIVES_SAVE_AS = ""
TAG_SAVE_AS = ""
TAGS_SAVE_AS = ""

# IMAGE PROCESSING PLUGIN
IMAGE_PROCESS = {
    "thumb": {
        "type": "image",
        "ops": ["crop 0 0 50% 50%", "scale_out 150 150 True", "crop 0 0 150 150"],
    },
    "article-image": {
        "type": "image",
        "ops": ["scale_in 300 300 True"],
    },
    "logo": {
        "type": "image",
        "ops": ["scale_in 200 200 True"],
    },
    "profile": {
        "type": "image",

    }
}


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# SEO PLUGIN SETTINGS
SEO_REPORT = False  # SEO report is enabled by default
SEO_ENHANCER = True  # SEO enhancer is disabled by default
SEO_ENHANCER_OPEN_GRAPH = True # Subfeature of SEO enhancer
SEO_ENHANCER_TWITTER_CARDS = False # Subfeature of SEO enhancer

# SITEMAP PLUGIN SETTINGS
SITEMAP = {"format": "xml","priorities":{"articles": 0.5,"indexes": 0.5,"pages": 0.5},"changefreqs": {"articles": "monthly","indexes": "daily","pages": "monthly"}}

# HEADER LINKS FOR TOP NAVIGATION BAR
LINKS = (
    ("About Me", "/#about-me"),
    ("Case Studies", "/category/case-studies.html"),
    ("Projects", "/category/projects.html"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)


#CLEANUP URLS
#ARTICLE_URL = '{slug}/'
#ARTICLE_SAVE_AS = '{slug}/index.html'
#PAGE_URL = '{slug}/'
#PAGE_SAVE_AS = '{slug}/index.html'
#CATEGORY_URL = "category/{slug}/"
#CATEGORY_SAVE_AS = "category/{slug}/index.html"
#CATEGORIES_URL = "category/"
#CATEGORIES_SAVE_AS = "category/index.html"


#DEVELOPMENT SETTINGS
LOAD_CONTENT_CACHE = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
