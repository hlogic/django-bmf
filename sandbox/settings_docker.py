from sandbox.settings_common import *

# OLD BELOW THIS LINE -----------------------------------------------------------------------------

# Django settings

import os

INSTALLED_APPS += (
    'celery',
)
INSTALLED_APPS += TEST_PROJECT_APPS

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake-439478'
    }
}

# BMF ==============================================================================

BMF_DOCUMENT_ROOT = os.path.join(PROJECT_PATH, "bmf_documents")
BMF_DOCUMENT_URL = '/bmf_documents/'

#import djcelery
#djcelery.setup_loader()
#CELERY_SEND_TASK_ERROR_EMAIL=True # ?????

# LOCAL SETTINGS ==================================================================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': '5432',
    }
}

BROKER_URL = 'redis://redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://redis:6379/0'
CELERY_ALWAYS_EAGER=False
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://elasticsearch:9200/',
        'INDEX_NAME': 'djangobmf',
    },
}

INSTALLED_APPS += (
#   'django_extensions',
    'debug_toolbar',
)
MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)
DEBUG_TOOLBAR_CONFIG = {
    'JQUERY_URL': None,
}

# OLD OVER THIS LINE ------------------------------------------------------------------------------

try:
    from sandbox.settings_local import *
except:
    pass