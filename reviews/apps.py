from django.apps import AppConfig
from django.db.models import BigAutoField

class ReviewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reviews'

