from django.apps import AppConfig


class CartConfig(AppConfig):
    name = 'cart'

    def ready(self):
        import cart.signals
