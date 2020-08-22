from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from basket.context import basket_ebooks

import stripe


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "Basket is empty!")
        return redirect(reverse('courses'))

    current_basket = basket_ebooks(request)
    total = current_basket['total']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51HHsLPHe52J6RnjHdH4B4wyvSY2jVlZxZeIABYuPmMtXHJ84S6cW7AruDORAxHFW7eUpcpVjwwTGQR0nPxBk7RXZ00diHfkSEQ',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)

