import os

DEBUG          = True
TEMPLATE_DEBUG = DEBUG
ROOTDIR        = os.path.abspath(os.path.dirname(__file__))

ADMINS   = (('teamaac', 'teamaac2012@gmail.com'),)
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'GL',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

TIME_ZONE                       = 'Africa/Tunis'
LANGUAGE_CODE                   = 'fr-fr'
USE_I18N                        = True
USE_L10N                        = True
USE_TZ                          = True
MEDIA_ROOT                      = os.path.join(ROOTDIR, '../media')
MEDIA_URL                       = '/media/'
STATIC_ROOT                     = os.path.join(ROOTDIR, '../static')
STATIC_URL                      = '/static/'
ADMIN_MEDIA_PREFIX              = '/static/admin/'
COVERAGE_CUSTOM_REPORTS         = True
COVERAGE_REPORT_HTML_OUTPUT_DIR = os.path.join(ROOTDIR, '../tests_report')
COVERAGE_MODULE_EXCLUDES        = ['admin', 'api', 'views']
ADMIN_TOOLS_MENU                = 'gestion.administration.menu.CustomMenu'
ADMIN_TOOLS_INDEX_DASHBOARD     = 'gestion.administration.dashboard.CustomIndexDashboard'
ADMIN_TOOLS_APP_INDEX_DASHBOARD = 'gestion.administration.dashboard.CustomAppIndexDashboard'

INTERNAL_IPS        = ('127.0.0.1',)
STATICFILES_DIRS    = ()
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = 'x!!gbc7=bcjj486w*nud(qzezaw18!q1i@%x#kw-p!777qa@_v'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
)

MIDDLEWARE_CLASSES = (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF     = 'GL.urls'
WSGI_APPLICATION = 'GL.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(ROOTDIR, '../templates')
)

INSTALLED_APPS = (
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django_coverage',
    'debug_toolbar',
    'autofixture',
    'tastytools',
    'annoying',
    'tastypie',
    'chartit',
    'gestion',
    'tdr',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
