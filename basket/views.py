from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from courses.models import Course


def view_basket(request):
    """ A view  that renders basket page """

    return render(request, 'basket/basket.html')


def add_to_basket(request, course_id):
    """ Add a quantity of the specified product to the shopping basket """
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})
    course = Course.objects.get(pk=course_id)

    if course_id not in basket:
        basket[course_id] = course_id

    else:
        basket[course_id] = course_id
        messages.success(request, f'Added {course.name} to your basket')

    request.session['basket'] = basket
    return redirect(redirect_url)


def delete_from_basket(request, course_id):
    """Delete item from cart"""

    course = Course.objects.get(pk=course_id)
    basket = request.session.get('basket', {})

    if course_id in basket:
        del basket[course_id]
        messages.success(request, f'Removed {course.name} from your bag')

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))
