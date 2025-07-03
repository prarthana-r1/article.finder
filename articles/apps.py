from django.apps import AppConfig
from django.db.models.signals import post_migrate

class ArticlesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'articles'

    def ready(self):
        from .scheduler import start_scheduler
        post_migrate.connect(start_scheduler, sender=self)
