from django.shortcuts import render, get_object_or_404

from .models import UserAccount


def myaccount(request):
    """ Display the user's account. """
    profile = get_object_or_404(UserAccount, user=request.user)


    template = 'myaccount/myaccount.html'
    context = {
         'myaccount': myaccount,
    }

    return render(request, template, context)