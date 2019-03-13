import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SECRET_KEY = 'not-really-secure'

DEBUG = os.environ.get('DEBUG', '0') == '1'

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = []

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'poincare_quotes.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'poincare_quotes.wsgi.application'
