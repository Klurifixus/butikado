from decouple import config

# Django settings
DEBUG = config('DEBUG', default=False, cast=bool)
SECRET_KEY = config('DJANGO_SECRET_KEY')
STRIPE_PUBLIC_KEY = config('STRIPE_PUBLIC_KEY', default='')
STRIPE_SECRET_KEY = config('STRIPE_SECRET_KEY', default='')

#SECRET_KEY=LkADxi9ZM0BHyp8js8KEcj_TvR9chKh9m3JbJOsFrO_tsalQvUK8ILqQapVtDjOxnuc