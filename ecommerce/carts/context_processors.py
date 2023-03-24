from .models import Cart, CartItem
from .views import _cart_id



def cart_counter(request):
    cart_count = 0
    #admin is the name of the admin url
    if 'admin' in request.path: # this condition is to prevent the cart counter from showing up in the admin panel
        return {}
    else :
        try:
            cart = Cart.objects.filter(cart_id=_cart_id(request))
            cart_items = CartItem.objects.all().filter(cart=cart[:1]) # [:1] is to get the first item in the cart
            for cart_item in cart_items:
                cart_count += cart_item.quantity
        except Cart.DoesNotExist:
            cart_count = 0
    return dict(cart_count=cart_count)                
    
    
    
    # add this to the settings.py file in the TEMPLATES section