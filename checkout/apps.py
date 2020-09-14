from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    name = 'checkout'

    def signals(self):
        import checkout.signals
