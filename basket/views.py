from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib import messages

from courses.models import Course


def view_basket(request):
    courses = Course.objects.all()

    context = {
        'courses': courses,
    }

    return render(request, 'basket/basket.html', context)

def add_to_basket(request, item_id):

    course = get_object_or_404(Course, pk=item_id)
    sub_total = course.price

    quantity = 1
    redirect_url = request.POST.get('redirect_url')
    default_values = {
        'course': course.id,
        'sub_total': float(sub_total),
        'quantity': quantity,
        'id': len(basket) + 1,
        }
    basket.append(default_values)
    messages.success(request, f'Added {course.name} to your basket')

    request.session['basket'] = basket
    print(request.session['basket'])
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
            messages.success(request, f'Removed {course.name} from your bag')
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing product {e}')
        return HttpResponse(status=500)
