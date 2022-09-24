import os.path
from pathlib import Path
import environ

env = environ.Env(
    DEBUG=(bool, False)
)

BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
DEBUG = env('DEBUG')
SECRET_KEY = env('KEY')

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'phonenumber_field',
    'modeltranslation',
    'pages_app.apps.PagesAppConfig',
    'cinema_app.apps.CinemaAppConfig',
    'user_app.apps.UserAppConfig',
    'my_admin.apps.MyAdminConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
    'channels',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'Cinema.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Cinema.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('name'),
        'USER': env('user'),
        'PASSWORD': env('db_password'),
        'HOST': env('host'),
        'PORT': '',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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

LANGUAGE_CODE = 'uk'
MODELTRANSLATION_DEFAULT_LANGUAGE = 'uk'
LANGUAGES = (
    ('uk', 'Ukrainian'),
    ('ru', 'Russian'),
)
LOCALE_PATHS = (
    'locale',
    )

TIME_ZONE = 'EET'

USE_I18N = True
USE_L18N = True
USE_L10N = True
USE_TZ = True
STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = env('email')
EMAIL_HOST_PASSWORD = env('email_password')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = 'media/'
AUTH_USER_MODEL = 'user_app.CustomUser'
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/user/login'
ASGI_APPLICATION = "Cinema.asgi.application"
DATE_INPUT_FORMATS = ('%d/%m/%Y','%d-%m-%Y','%Y-%m-%d')
DATE_FORMAT = '%d/%m/%Y'
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [(env('redis_host'), env('redis_channel'))],

        },
    },
}


