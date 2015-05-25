from .base import *

DEBUG = True

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = "dauxerdocs@gmail.com"
EMAIL_HOST_PASSWORD = "44r0nIsAtw@t"
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'dauxerdocs@gmail.com'


try:
	from .local import *
except ImportError:
	pass
