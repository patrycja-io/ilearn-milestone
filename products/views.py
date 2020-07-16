from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product

# Create your views here.
    def all_products(request):
    """ """
        products = Product.objects.all()

        if request.GET:
            if 'q' in request.GET:
                query = request.GET['q']
                if not query:
                    messages.error(request, "You didn't enter any search criteria!")
                    return redirect(reverse('products'))

    context = { 
        'products' : products,

    }

    return render(request, 'products/products.html', context)

def product_detail(request, product_id):
    
