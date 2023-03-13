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


def product_details(request,product_slug,category_slug):
    
    try:
        single_product = Product.objects.get(product_slug=product_slug, product_category__categorySlug=category_slug)
        in_stock = Product.objects.filter(product_isavilabe=True).count()
    except Exception as e:
        raise e
    
    context = {
        "single_product": single_product,
        "in_stock": in_stock,
    }
    return render(request, 'store/product_details.html', context)
    
