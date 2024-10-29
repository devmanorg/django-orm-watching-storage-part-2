import os
from environs import Env


env = Env()
DATABASES = {
    'default': {
        'ENGINE': env('SETTING_ENGINE'),
        'HOST': env('SETTING_HOST'),
        'PORT': env('SETTING_PORT'),
        'NAME': env('SETTING_NAME'),
        'USER': env('SETTING_USER'),
        'PASSWORD': env('SETTING_PASSWORD'),
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = env('SETTING_SECRET_KEY')

DEBUG = env('SETTING_DEBUG')

ROOT_URLCONF = env('SETTING_ROOT_URLCONF')

ALLOWED_HOSTS = [env('SETTING_ALLOWED_HOSTS')]


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
