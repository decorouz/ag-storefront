from django.dispatch import Signal

order_created = Signal()

# this declares an order_created signal
# Next we need to fire the signal when an order is created
