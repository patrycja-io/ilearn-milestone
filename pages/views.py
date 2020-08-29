from django.shortcuts import render
from courses.models import Course

# Create your views here.


def home(request, *args, **kwargs):
    """ Renders home page with 6 random featured products in featured
          listing section """

    featured_products = Course.objects.filter(featured=True).order_by('?')[:6]
    context = {
        'featured_products': featured_products,
        'category': 'All Products',
        'page': 'home',
    }
    return render(request, "index.html", context)


def about(request, *args, **kwargs):
    return render(request, "about.html")


def contact(request, *args, **kwargs):
    return render(request, "contact.html")


def terms(request, *args, **kwargs):
    return render(request, "terms.html")
