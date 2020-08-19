from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "Basket is empty!")
        return redirect(reverse('courses'))

    order_form = OrderForm()
    template = 'checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51HHsLPHe52J6RnjHdH4B4wyvSY2jVlZxZeIABYuPmMtXHJ84S6cW7AruDORAxHFW7eUpcpVjwwTGQR0nPxBk7RXZ00diHfkSEQ',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)