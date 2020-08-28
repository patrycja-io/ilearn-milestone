from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserAccount
from .forms import UserAccountForm

from checkout.models import Order

@login_required
def myprofile(request):
    """ Display the user's profile. """
    myprofile = get_object_or_404(UserAccount, user=request.user)

    if request.method == 'POST':
        form = UserAccountForm(request.POST, instance=myaccount)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account updated successfully')

    form = UserAccountForm(instance=myaccount)
    orders = myaccount.orders.all()

    template = 'myaccount/myaccount.html'
    context = {
        'form': form,
        'orders': orders,
        'on_myaccount_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_myaccount': True,
    }

    return render(request, template, context)