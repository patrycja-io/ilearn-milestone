from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def cart(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "There's nothing in your basket yet")
        return redirect(reverse('courses'))

    order_form = OrderForm()
    template = 'cart/cart.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)