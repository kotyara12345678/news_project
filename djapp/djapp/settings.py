from pathlib import Path
import os

# --- Базовые пути ---
BASE_DIR = Path(__file__).resolve().parent.parent

# --- Секретный ключ и DEBUG ---
SECRET_KEY = os.getenv(
    "DJANGO_SECRET_KEY",
    "django-insecure-u@*+m6*-u-78=2(vc+jp3(3nv(+45o!^&naboi+4adk@t+g%2o"
)

DEBUG = os.getenv("DEBUG", "False") == "True"  # Для продакшена False

# --- Разрешённые хосты ---
ALLOWED_HOSTS = ['.onrender.com', 'localhost']

# --- Установленные приложения ---
INSTALLED_APPS = [
    'nain',
    'news',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# --- Middleware ---
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# --- Корневой URL конфиг ---
ROOT_URLCONF = 'djapp.urls'

# --- Шаблоны ---
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # общие шаблоны
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# --- WSGI ---
WSGI_APPLICATION = 'djapp.wsgi.application'

# --- База данных (SQLite по умолчанию) ---
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# --- Валидаторы паролей ---
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# --- Локализация ---
LANGUAGE_CODE = 'ru'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_TZ = True

# --- Статика ---
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [BASE_DIR / 'static']

# --- Медиа ---
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# --- Поля авто-инкремента по умолчанию ---
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'