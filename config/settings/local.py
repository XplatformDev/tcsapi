from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'jn%jjmqhu_62$ytj0(@8431$&u)9ac_zdc#f@06vd4k4rrt02t'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DJANGO_DEBUG', True)