from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from .models import UserAccount
from .forms import UserAccountForm


def myaccount(request):
    """ Display the user's profile. """
    myaccount = get_object_or_404(UserAccount, user=request.user)

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