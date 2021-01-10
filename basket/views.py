from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib import messages
from courses.models import Course


def view_basket(request):
    return render(request, 'basket/basket.html', context)

def add_to_basket(request, item_id):

    course = get_object_or_404(Course, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    if item_id in list(basket.keys()):
            basket[item_id] += quantity
            messages.success(request,
                             (f'Updated {course.name} '
                              f'quantity to {basket[item_id]}'))
                              
        else:
            basket[item_id] = quantity
            messages.success(request, f'Added {course.name} to your basket')

    request.session['basket'] = basket
    return redirect(redirect_url)

def delete_from_basket(request, item_id):
    """Delete item from cart"""

    try:
        basket = request.session.get('basket', [])
        removed_item = None
        new_basket = []

        for item in basket:
            if item['id'] == int(item_id):
                removed_item = item
                continue
            new_basket.append(item)

        request.session['basket'] = new_basket
        if removed_item:
            course = Course.objects.get(id=removed_item['course'])
            messages.success(request, f'Removed {course.name} from your basket')
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing product {e}')
        return HttpResponse(status=500)
