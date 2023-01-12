from django.apps import AppConfig

class Myapp3Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp3'
    def ready(self):
        from .ap_scheduler import start
        start()