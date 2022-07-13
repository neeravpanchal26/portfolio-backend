from .base import *

DEBUG = False

ALLOWED_HOSTS = ['https://neeravpanchal26.pythonanywhere.com/']

ROOT_CONF = "mycms.urls"

SECRET_KEY = ')iij*sov_i7sp0yp*=_@ngu1n@szcbc79^2^#8$53-i7#(lc!u'

try:
    from .local import *
except ImportError:
    pass
