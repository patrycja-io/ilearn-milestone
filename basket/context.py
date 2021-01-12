from django.conf import settings
from django.shortcuts import get_object_or_404
from courses.models import Course


def basket_contents(request):

    basket_items = []
    total = 0
    product_count = 0
    basket = request.session.get('basket', [])

    for values in basket:
        item_id = values['product']
        product = get_object_or_404(Product, pk=item_id)
        sub_total = product.price
        total += values['quantity'] * product.price
       
        product_count += values['quantity']
        basket_items.append({
            'sub_total': sub_total,
            'item_id': item_id,
            'quantity': values['quantity'],
            'product': product,
            'background': values['background'],
            'extra_requirements': values['extra_requirements'],
            'text_color': values['text_color'],
            'text_content': values['text_content'],
            'id': values['id'],
        })

    context = {
        'basket_items': basket_items,
        'total': total,
        'product_count': product_count,
        'bundle_discount_threshold': settings.BUNDLE_DISCOUNT_THRESHOLD,
        'grand_total': grand_total,
        'discount': float(total) - float(grand_total),
    }

    return context