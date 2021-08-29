import os
from pathlib import Path
from datetime import timedelta
import my_settings # my_setting.py의 설정을 적용하기 위해 임포트


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = my_settings.SECRET['secret']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition
# 사용하지 않는 앱과 middleware는 주석처리 해놓기!!

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'rest_framework',
    'rest_framework_jwt',

    'drf_yasg',
    'ckeditor',
    'corsheaders', # CORS 관련 추가

    # my app
    'mypage',
    'post',
    'recipe',
    'core',
    'account',
    'music',
    'mbti',
]

SITE_ID = 1

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware', # CORS 관련 추가
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

#REMOVE_APPEND_SLASH_WARNING                                   
APPEND_SLASH = False

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = my_settings.DATABASES


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_USER_MODEL = 'account.User'

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CORS 관련 추가 
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL=True

CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
)

CORS_ALLOW_HEADERS = (
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    # 만약 허용해야할 추가적인 헤더키가 있다면?(사용자정의 키) 여기에 추가하면 됩니다.
)

MEDIA_URL = '/media/' # 필드명.url 속성으로 참조할 수 있음
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') # 실제 파일 저장 root경로

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
}


#JWT 환경 설정
REST_USE_JWT = True

# 추가 설정 부분

SIMPLE_JWT = {
   
   # 여기는 기본 세팅값
   'JWT_SECRET_KEY': SECRET_KEY,   # JWT 에 서명하는데 사용되는 시크릿키. 장고의 시크릿키가 디폴트.
   'JWT_ALGORITHM': 'HS256',       # PyJWT 에서 암호화 서명에 지원되는 알고리즘으로 마찬가지로 이것 또한 기본값.
   'JWT_VERIFY_EXPIRATION' : True, # 토큰 만료 시간 확인. 기본값 True.    

   # 새로 커스텀한 옵션들
   'JWT_ALLOW_REFRESH': True,      # 토큰 새로고침 기능 활성화. 기본값 False.
   'JWT_EXPIRATION_DELTA': timedelta(minutes=30),     # datetime.timedelta 의 만료 시간. 기본값 seconds=300. 
   'JWT_REFRESH_EXPIRATION_DELTA': timedelta(days=3), # Refresh Token의 새로 고침 시간. 기본값 days=7
   'JWT_RESPONSE_PAYLOAD_HANDLER': 'accounts.custom_responses.my_jwt_response_handler',  #로그인 또는 새로 고침 후 반환되는 응답 데이터를 제어. 기본값은 {'token' : token } 인데 이건 나중에 우리가 따로 적어줄것임.
}

SWAGGER_SETTINGS = {
   'SECURITY_DEFINITIONS': {
      'Basic': {
            'type': 'basic'
      },
      'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
      }
   }
}
