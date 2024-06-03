from core.settings import * 
from decouple import config




# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-t8_r3fao0u3x)f(x13t0soizooczzxh*&=5mbm=_v2qz&-#%h1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# sitemap framework
SITE_ID = 2



INSTALLED_APPS = [
    'debug_toolbar',
]

# INTERNAL_IPS = [
#     "127.0.0.1",
# ]




# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
# DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.sqlite3',
#             'NAME': BASE_DIR / 'db.sqlite3',
#         }
#     }
if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
    'default': {
        'ENGINE': config("DB_ENGINE"),
        'NAME': config("DB_NAME"),
        'USER': config("DB_USER"),
        'PASSWORD':config("DB_PASSWORD"),
        'HOST': config("DB_HOST"),
        'PORT': config("DB_PORT",cast=int),
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
STATIC_ROOT = BASE_DIR / 'static'
MEDIA_ROOT = BASE_DIR / 'media'

# STATIC_ROOT = BASE_DIR / 'static'
# MEDIA_ROOT = BASE_DIR / 'media'
STATICFILES_DIRS = [
    BASE_DIR / "statics"
]
# compressor
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
]

COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True

# Set the backend to use for compression
COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    'compressor.filters.cssmin.CSSMinFilter',
]

COMPRESS_JS_FILTERS = [
    'compressor.filters.jsmin.JSMinFilter',
]

# Cache settings for compressor
COMPRESS_CACHE_BACKEND = 'default'


# security config for production
# deploy 
if config("USE_SSL_SETTINGS",cast=bool, default=False):
    # Https settings
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True
    SECURE_SSL_REDIRECT = True
    
    # HTTPS SETTINGS
    SECURE_HSTS_SECONDS = 315360000
    SECURE_HSTS_PRELOAD = True
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True

    # MORE SECURITY SETTING
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_BROWSER_XSS_FILTER = True
    X_FRAME_OPTIONS = 'SAMEORIGIN'
    SECURE_REFERRER_POLICY = "strict-origin"
    USE_X_FORWARDED_HOST = True
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
