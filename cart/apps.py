from django.apps import AppConfig


class CartConfig(AppConfig):
    name = 'check'

    def ready(self):
        import check.signals
