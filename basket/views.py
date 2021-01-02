from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages

from courses.models import Course


def view_basket(request):
    courses = Course.objects.all()

    context = {
        'courses': courses,
    }

    return render(request, 'basket/basket.html', context)



def add_to_basket(request, item_id):
    """ Add a quantity of the specified product to the shopping basket """
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})
    course = get_object_or_404(Course, pk=item_id)

    if item_id not in basket:
        basket[item_id] = item_id

    else:
        basket[item_id] = item_id
        messages.success(request, f'Added {course.name} to your basket')

    request.session['basket'] = basket
    return redirect(redirect_url)


def delete_from_basket(request, item_id):
    """Delete item from cart"""

    course = get_object_or_404(Course, pk=item_id)
    basket = request.session.get('basket', [])

    if item_id in basket:
        del basket[item_id]
        messages.success(request, f'Removed {course.name} from your bag')

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))
