from django.shortcuts import render


def account(request):
    """ Display the user's account. """

    template = 'accounts/accounts.html'
    context = {}

    return render(request, template, context)