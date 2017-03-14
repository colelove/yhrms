# -*-coding:utf-8-*-
"""
Django settings for YHRM project.

Generated by 'django-admin startproject' using Django 1.8.16.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&g3w65y+3)dho)4dihh77t%yj_m=g#-6+934ne@*$ljej@1lyo'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = (

    'debugtools',
    'table',
    'bootstrapform',
    'suit',
    # 'suit_dashboard',
    'simple_history',
    'import_export',
    'report_builder',
    # django it self

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # your applications
    'base_site',
    'department',
    'employee',
    'leave',
    'payroll',
    'explorer',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    # simple history
    'simple_history.middleware.HistoryRequestMiddleware',
)

ROOT_URLCONF = 'YHRM.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.static',
                'django.core.context_processors.media',

            ],
        },
    },
]
SUIT_CONFIG = {
    # header
    'ADMIN_NAME': u'人事管理系统后台',
    'HEADER_DATE_FORMAT': 'l, Y   F   j ',
    # 'HEADER_TIME_FORMAT': 'H:i',

    # forms
    'SHOW_REQUIRED_ASTERISK': True,  # Default True
    'CONFIRM_UNSAVED_CHANGES': True,  # Default True
    'SEARCH_URL': '',

    'MENU_OPEN_FIRST_CHILD': True,
    # 'MENU_EXCLUDE': ('auth.group',),

}

WSGI_APPLICATION = 'YHRM.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
#

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'yhrm',  # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',  # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '3306',  # Set to empty string for default.
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'statics')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'media'),
)
LOGIN_URL = '/login'
AUTH_USER_MODEL = "base_site.UserProfile"
# session
SESSION_COOKIE_AGE = 60 * 30
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
FILTERS_DISABLE_HELP_TEXT = True
REPORT_BUILDER_INCLUDE = ['department.Department', 'employee.Employee', 'employee.Contract',
                          'employee.Eduction', 'employee.WorkExperience', 'employee.RelationShip',
                          'employee.Remark', 'employee.TransferOrder']