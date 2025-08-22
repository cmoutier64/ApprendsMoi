from pathlib import Path
import os, dj_database_url
BASE_DIR=Path(__file__).resolve().parent.parent
SECRET_KEY=os.getenv('DJANGO_SECRET_KEY','dev-secret-key')
DEBUG=os.getenv('DEBUG','1')=='1'
ALLOWED_HOSTS=os.getenv('ALLOWED_HOSTS','localhost,127.0.0.1').split(',')
INSTALLED_APPS=['django.contrib.admin','django.contrib.auth','django.contrib.contenttypes','django.contrib.sessions','django.contrib.messages','django.contrib.staticfiles','core']
MIDDLEWARE=['django.middleware.security.SecurityMiddleware','whitenoise.middleware.WhiteNoiseMiddleware','django.contrib.sessions.middleware.SessionMiddleware','django.middleware.common.CommonMiddleware','django.middleware.csrf.CsrfViewMiddleware','django.contrib.auth.middleware.AuthenticationMiddleware','django.contrib.messages.middleware.MessageMiddleware','django.middleware.clickjacking.XFrameOptionsMiddleware']
ROOT_URLCONF='app.urls'
TEMPLATES=[{'BACKEND':'django.template.backends.django.DjangoTemplates','DIRS':[BASE_DIR/'templates'],'APP_DIRS':True,'OPTIONS':{'context_processors':['django.template.context_processors.debug','django.template.context_processors.request','django.contrib.auth.context_processors.auth','django.contrib.messages.context_processors.messages']}}]
WSGI_APPLICATION='app.wsgi.application'
ASGI_APPLICATION='app.asgi.application'
if os.getenv('DATABASE_URL'):
    DATABASES={'default': dj_database_url.config(conn_max_age=600, ssl_require=True)}
else:
    DATABASES={'default':{'ENGINE':'django.db.backends.sqlite3','NAME':BASE_DIR/'db.sqlite3'}}
STATIC_URL='/static/'
STATIC_ROOT=BASE_DIR/'staticfiles'
STATICFILES_DIRS=[BASE_DIR/'static'] if (BASE_DIR/'static').exists() else []
STORAGES={'staticfiles':{'BACKEND':'whitenoise.storage.CompressedManifestStaticFilesStorage'}}
if os.getenv('S3_BUCKET'):
    INSTALLED_APPS+=['storages']
    DEFAULT_FILE_STORAGE='storages.backends.s3boto3.S3Boto3Storage'
    AWS_S3_ENDPOINT_URL=os.getenv('S3_ENDPOINT')
    AWS_STORAGE_BUCKET_NAME=os.getenv('S3_BUCKET')
    AWS_ACCESS_KEY_ID=os.getenv('S3_KEY')
    AWS_SECRET_ACCESS_KEY=os.getenv('S3_SECRET')
    AWS_S3_REGION_NAME=os.getenv('S3_REGION','auto')
AUTH_PASSWORD_VALIDATORS=[{'NAME':'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},{'NAME':'django.contrib.auth.password_validation.MinimumLengthValidator'},{'NAME':'django.contrib.auth.password_validation.CommonPasswordValidator'},{'NAME':'django.contrib.auth.password_validation.NumericPasswordValidator'}]
LANGUAGE_CODE='fr-fr'
TIME_ZONE='Europe/Paris'
USE_I18N=True
USE_TZ=True
DEFAULT_AUTO_FIELD='django.db.models.BigAutoField'
