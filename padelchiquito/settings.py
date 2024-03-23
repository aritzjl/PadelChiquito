"""
Django settings for padelchiquito project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-+^m)ej)i9tvh#e1fdvwelwd1i$*(u%a!+a35z$x*q(k9im2k6g'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['178.16.131.191','www.padelchiquito.com','padelchiquito.com','127.0.0.1','https://www.padelchiquito.com']

CSRF_TRUSTED_ORIGINS = [
'https://www.padelchiquito.com',   
'https://padelchiquito.com',
]

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# Ruta donde se almacenarán las imágenes cargadas
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# URL base para las imágenes cargadas
MEDIA_URL = '/media/'
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'django.contrib.sites',
    
    #Third apps
    "debug_toolbar",
    
    #CKEditor apps
    'ckeditor',
    'ckeditor_uploader',
    'ckeditor_skins',
    
    #Started apps
    'apps.comparador',
    'apps.reviews',
    'apps.valoraciones',
    'apps.users',
    'apps.entrenamientos',
    'apps.blog',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
    #third apps
     
]
CKEDITOR_UPLOAD_PATH = "blog/"

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'skin': 'prestige',
        'extraPlugins': ','.join([
            'dialog',
            'dialogui',
            'elementspath',
            'entities',
            'fakeobjects',
            'filebrowser',
            'image',
            'link',
            'showblocks',
            'wysiwygarea',
            'sourcearea',
            'codesnippet',
        ]),
        'contentsCss': ['/static/css/output.css'],  # Ruta a tu archivo CSS de Tailwind
        'format_tags': 'p;h1;h2;h3;pre',
        'width': '100%',
        'height': 300,
        "removePlugins": "stylesheetparser",
        'allowedContent': True,
        'enterMode': 2,  # Cambia esto si prefieres otro modo de inserción de párrafos
        'bodyClass': 'font-sans',  # Clase de Tailwind para el cuerpo del editor
        'bodyId': 'ckeditor_body',
        'stylesSet': 'my_styles',
    }
}

#DEBUG TOOLBAR
INTERNAL_IPS = [
    # ...
    #"127.0.0.1",
    # ...
]

SHOW_TOOLBAR_CALLBACK=True
DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.history.HistoryPanel',
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
    'debug_toolbar.panels.profiling.ProfilingPanel',
]

ROOT_URLCONF = 'padelchiquito.urls'

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = 'padelchiquito.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases




# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

LOGIN_URL = '/signin/'  # Ruta a la página de inicio de sesión




EMAIL_SENDER = "hello@padelchiquito.com"
EMAIL_PASS = "Aritz@Javi12"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

# This setting tells Django at which URL static files are going to be served to the user.
# Here, they well be accessible at your-domain.onrender.com/static/...
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT =  '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

