from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from courses.models import Course



def basket_ebooks(request):

    basket_items = []
    total = 0
    product_count = 0
    basket = request.session.get('basket', {})

    for item_id in basket.items():
        course = get_object_or_404(Course, pk=item_id)
        basket_items.append({
            'item_id': item_id,
            'course': course,
        })

    grand_total = total

    context = {
        'basket_items': basket_items,
        'total': total,
        'course_count': product_count,
        'grand_total': grand_total,
    }

    return context
