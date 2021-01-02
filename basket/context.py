from django.shortcuts import get_object_or_404
from courses.models import Course


def basket_ebooks(request):

    basket_items = []
    total = 0
    product_count = 0
    basket = request.session.get('basket', [])

    for values in basket:
        course_id = data.values[]
        course = get_object_or_404(Course, pk=course_id)
        sub_total = course.price
        total += values['quantity'] * course.price

        product_count += values['quantity']
        basket_items.append({
            'sub_total': sub_total,
            'course_id': course_id,
            'quantity': values['quantity'],
            'course': course,
            'id': values['id'],
        })

        grand_total = total
        grand_total = float(total) * 0.8

    context = {
        'basket_items': basket_items,
        'total': total,
        'product_count': product_count,
        'grand_total': grand_total,
    }

    return context
