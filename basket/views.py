from django.shortcuts import render


def view_basket(request):
    """ A view  that renders basket page """

    return render(request, 'basket/basket.html')