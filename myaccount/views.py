from django.shortcuts import render


def myaccount(request):
    """ Display the user's account. """

    template = 'myaccount/myaccount.html'
    context = {}

    return render(request, template, context)