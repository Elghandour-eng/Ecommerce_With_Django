from django.shortcuts import render , get_object_or_404
from .models import Product 
from category.models import Category

# Create your views here.

def store(request , category_slug=None):
    products = None
    categories = None
    
    if category_slug != None:
        categories = get_object_or_404(Category, categorySlug=category_slug)
        products = Product.objects.all().filter(product_category=categories, product_isavilabe=True)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(product_isavilabe=True)
        product_count = products.count()

    
    context = {
        "products": products,
        "product_count": product_count,
    }
    return render(request, 'store/store.html', context)
