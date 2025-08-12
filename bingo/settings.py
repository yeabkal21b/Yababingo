AUTH_USER_MODEL = 'bingo.User'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'yaba_bingo',
    'USER': 'postgres',
    'PASSWORD': 'YOUR_PASSWORD',
    'HOST': 'localhost',
    'PORT': '5432',
  }
}

CORS_ALLOWED_ORIGINS = [
    "https://your-render-frontend-url.onrender.com",
]```

### `requirements.txt`