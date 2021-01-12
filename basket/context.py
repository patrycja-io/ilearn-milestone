from django.conf import settings
from django.shortcuts import get_object_or_404
from courses.models import Course


def basket_contents(request):

    basket_items = []
    total = 0
    course_count = 0
    basket = request.session.get('basket', [])

    for values in basket:
        item_id = values['course']
        course = get_object_or_404(Course, pk=item_id)
        sub_total = course.price
        total += values['quantity'] * course.price
       
        course_count += values['quantity']
        basket_items.append({
            'sub_total': sub_total,
            'item_id': item_id,
            'quantity': values['quantity'],
            'course': course,
            'id': values['id'],
        })

    
        grand_total = float(total) * 0.8

    context = {
        'basket_items': basket_items,
        'total': total,
        'course_count': course_count,
        'grand_total': grand_total,

    }

    return context