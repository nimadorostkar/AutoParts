import os
from pathlib import Path




# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1^%12q4s7^@86prla^qv16*i0-&ml0zx8e+t^(hm66-q&v5#+3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = ['*']


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # my library
    'ckeditor',
    'django_render_partial',
    'ckeditor_uploader',
    'django_ckeditor_5',
    'mptt',
    'django.contrib.humanize',
    'django_filters',
    'captcha',
    'extensions',
    # rest api
    'rest_framework',
    'rest_framework.authtoken',
    'drf_yasg',
    # my app
    'eshop_account',
    'eshop_attribute',
    'eshop_brand',
    'eshop_category',
    'eshop_comment',
    'eshop_contact',
    'eshop_image',
    'eshop_order',
    'eshop_product',
    'eshop_setting',
    'eshop_slider',
    'eshop_tag',
    'eshop_variant',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'didikala.urls'

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
                'django.template.context_processors.request'
            ],
            'libraries': {
                # make your file entry here.
                'filter_tags': 'templatefilter.filters_tem',
            }
        },
    },
]

WSGI_APPLICATION = 'didikala.wsgi.application'

#DEFAULT_AUTO_FIELD='django.db.models.AutoField'
DEFAULT_AUTO_FIELD='django.db.models.BigAutoField'





# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}





# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'fa-ir'

TIME_ZONE = 'Asia/Tehran'

USE_I18N = True

USE_L10N = True

USE_TZ = True




# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, "assets")]
STATIC_ROOT = os.path.join(BASE_DIR, "static", "static_root")

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
# ...
SITE_ID = 1



####################################
##  CKEDITOR CONFIGURATION ##
####################################

CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js'
CKEDITOR_UPLOAD_PATH = 'media_ckeditor/'
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': None,
    },
}

RECAPTCHA_PUBLIC_KEY = '6Le4K_4ZAAAAAFlxvlemZk5oeKMgrXrmNMtbbZLT'
RECAPTCHA_PRIVATE_KEY = '6Le4K_4ZAAAAAIE5eYCdFbJrdfSOJUuuASyRVIfX'
SILENCED_SYSTEM_CHECKS = ['captcha.recaptcha_test_key_error']



# REST_FRAMEWORK CONFIGURATION

REST_FRAMEWORK = {
     'DEFAULT_AUTHENTICATION_CLASSES': [
         'rest_framework.authentication.SessionAuthentication',
         'rest_framework.authentication.TokenAuthentication',
     ],
     'DEFAULT_PERMISSION_CLASSES': [
         'rest_framework.permissions.IsAuthenticatedOrReadOnly',
     ],
     'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
     'PAGE_SIZE': 5,
     'DEFAULT_FILTER_BACKENDS': (
     'django_filters.rest_framework.DjangoFilterBackend',
    ),
}



# ZARRINPAL CONFIGURATION
ZARRINPAL_URL="https://api.zarinpal.com/pg/"
ZARRINPAL_MERCHANT_ID = "c0b8169f-deb9-46a2-a1c3-7f45f9df1e4a"
ZP_API_REQUEST = "https://www.zarinpal.com/pg/rest/WebGate/PaymentRequest.json"
ZP_API_VERIFY = "https://www.zarinpal.com/pg/rest/WebGate/PaymentVerification.json"
ZP_API_STARTPAY = "https://www.zarinpal.com/pg/StartPay/"
ZARIN_CALL_BACK = 'http://127.0.0.1:8000/pay_verify/'
# END ZARRINPAL CONFIGURATION
