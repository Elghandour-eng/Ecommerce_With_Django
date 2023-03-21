from django.urls import path
from . import views




urlpatterns = [
    path("",views.cart_home,name="carts"),
    path("add/<int:product_id>/",views.add_to_cart,name="add_to_cart"),
 ]