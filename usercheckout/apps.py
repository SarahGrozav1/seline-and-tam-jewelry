from django.apps import AppConfig


class UsercheckoutConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'usercheckout'
    
    def ready(self):
        import checkout.signals
