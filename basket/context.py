from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from courses.models import Course


def basket_contents(request):

    basket_items = set()
    total = 0
    basket = request.session.get('basket', {})

    for course_id in basket.keys():
        course = get_object_or_404(Course, pk=course_id)
        total += course.price
        basket_items.add(course)

    context = {
        'basket_items': basket_items,
        'total': total,
    }

    return context
