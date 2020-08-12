from django.shortcuts import render, redirect


def view_basket(request):
    """ A view  that renders basket page """

    return render(request, 'basket/basket.html')

def add_to_basket(request, course_id):
    """ Add a quantity of the specified product to the shopping basket """
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {}) 

    if course_id not in basket:
        basket[course_id] = course_id

    request.session['basket'] = basket
    return redirect(redirect_url) 


