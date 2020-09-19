from .base import *  # noqa

env = environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, 'config/.env.dev'))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
