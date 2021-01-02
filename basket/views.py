from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages

from courses.models import Course


def view_basket(request):
    """ A view  that renders basket page """
    return render(request, 'basket/basket.html')


def add_to_basket(request, course_id):
    """ Add a quantity of the specified product to the shopping basket """
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', [])
    course = get_object_or_404(Course, pk=course_id)

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
    basket = request.session.get('basket', [])

    if course_id in basket:
        del basket[course_id]
        messages.success(request, f'Removed {course.name} from your bag')

    request.session['basket'] = basket
    return redirect(reverse('view_basket'))

def add_to_bag(request, item_id):

    product = get_object_or_404(Product, pk=item_id)
    sub_total = product.price

    quantity = 1
    redirect_url = request.POST.get('redirect_url')
    background = request.POST.get('background')
    extra_requirements = request.POST.get('extra_requirements')
    text_color = request.POST.get('text_color')
    text_content = request.POST.get('text_content')
    bag = request.session.get('bag', [])
    if extra_requirements:
        sub_total += 5

    sub_total += Personalise.EXTRA_COST[background]
    sub_total += Personalise.EXTRA_COST[text_color]
    default_values = {
        'product': product.id,
        'sub_total': float(sub_total),
        'quantity': quantity,
        'background': background,
        'extra_requirements': extra_requirements,
        'text_color': text_color,
        'text_content': text_content,
        'id': len(bag) + 1,
        }
    bag.append(default_values)
    messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)





def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        bag = request.session.get('bag', [])
        removed_item = None
        new_bag = []

        for item in bag:
            if item['id'] == int(item_id):
                removed_item = item
                continue
            new_bag.append(item)

        request.session['bag'] = new_bag
        if removed_item:
            product = Product.objects.get(id=removed_item['product'])
            messages.success(request, f'Removed {product.name} from your bag')
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing product {e}')
        return HttpResponse(status=500
