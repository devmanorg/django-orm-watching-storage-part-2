import os
from environs import Env


env = Env()
DATABASES = {
    'default': {
        'ENGINE': env.str('SETTING_ENGINE'),
        'HOST': env.str('SETTING_HOST'),
        'PORT': env.str('SETTING_PORT'),
        'NAME': env.str('SETTING_NAME'),
        'USER': env.str('SETTING_USER'),
        'PASSWORD': env.str('SETTING_PASSWORD'),
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = env.str('SETTING_SECRET_KEY')

DEBUG = env.bool('SETTING_DEBUG')

ROOT_URLCONF = env.str('SETTING_ROOT_URLCONF')

ALLOWED_HOSTS = env.list('SETTING_ALLOWED_HOSTS')


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
