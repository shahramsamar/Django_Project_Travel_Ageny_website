from core.settings import * 




# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-t8_r3fao0u3x)f(x13t0soizooczzxh*&=5mbm=_v2qz&-#%h1'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = False



ALLOWED_HOSTS = ['*']
# ALLOWED_HOSTS = ['my-project-final.liara.run']
# sitemap framework
SITE_ID = 2



# INSTALLED_APPS = [
# ]


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
# if DEBUG:
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.sqlite3',
#             'NAME': BASE_DIR / 'db.sqlite3',
#         }
#     }
# else:
#     DATABASES = {
#     'default': {
#         'ENGINE': "django.db.backends.postgresql",
#         'NAME': "postgresql",
#         'USER': "postgresql",
#         'PASSWORD': "postgresql",
#         'HOST': "127.0.0.1",
#         'PORT': "5432",
#     }
# }

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
STATIC_ROOT = BASE_DIR / 'static'
MEDIA_ROOT = BASE_DIR / 'media'

# STATIC_ROOT = BASE_DIR / 'static'
# MEDIA_ROOT = BASE_DIR / 'media'
STATICFILES_DIRS = [
    BASE_DIR / "statics"
]
