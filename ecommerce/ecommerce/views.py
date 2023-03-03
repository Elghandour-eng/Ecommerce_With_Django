#from django.http import HttpResponse
from django.shortcuts import render
from store.models import Product


def home(request):
    products = Product.objects.all().filter(product_isavilabe = True)
    
    context = {
        "products": products
    }
    
    return render(request, "home.html" , context)