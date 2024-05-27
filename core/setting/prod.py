from core.settings import * 
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-t8_r3fao0u3x)f(x13t0soizooczzxh*&=5mbm=_v2qz&-#%h1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# sitemap framework
SITE_ID = 2



# INSTALLED_APPS = [
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
        'ENGINE': "django.db.backends.postgresql",
        'NAME': "postgresql",
        'USER': "postgresql",
        'PASSWORD': "postgresql",
        'HOST': "127.0.0.1",
        'PORT': "5432",
    }
}
    
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
# STATIC_ROOT = BASE_DIR / 'static'
# MEDIA_ROOT = BASE_DIR / 'media'

STATIC_ROOT = BASE_DIR / 'static'
MEDIA_ROOT = BASE_DIR / 'media'
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

# deploy 
CSRF_COOKIE_SECURE = True

## X-XSS-Protection
SECURE_BROWSER_XSS_FILTER = True

# ## X-Frame-Options
# X_FRAME_OPTIONS = 'SAMEORIGIN'
# #X-Content-Type-Options
# SECURE_CONTENT_TYPE_NOSNIFF = True
# ## Strict-Transport-Security
# SECURE_HSTS_SECONDS = 15768000
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_HSTS_PRELOAD = True

# ## that requests over HTTP are redirected to HTTPS. aslo can config in webserver
# SECURE_SSL_REDIRECT = True 

# # for more security
# CSRF_USE_SESSIONS = True
# CSRF_COOKIE_HTTPONLY = True
# SESSION_COOKIE_SECURE = True
# SESSION_COOKIE_SAMESITE = 'Strict'

# SECURE_CONTENT_TYPE_NOSNIFF = True
# SECURE_BROWSER_XSS_FILTER = True
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
# SECURE_SSL_REDIRECT = True
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# CSRF_TRUSTED_ORIGINS = ['127.0.0.1']