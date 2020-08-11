from django.shortcuts import render


def view_basket(request):
    """ A view  that renders basket page """

    return render(request, 'basket/basket.html')

def add_to_basket(request, item_id):
    """ Add a quantity of the specified product to the shopping basket """

    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {}) 

    request.session['basket'] = basket
    print(request.session['basket'])
    return redirect(redirect_url)   