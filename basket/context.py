from decimal import Decimal
from django.conf import settings


def basket_ebooks(request):

    basket_items = []
    total = 0
    product_count = 0

    grand_total = total

    context = {
        'basket_items': basket_items,
        'total': total,
        'course_count': product_count,
        'grand_total': grand_total,
    }

    return context
