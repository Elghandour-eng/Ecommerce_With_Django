from django.db import models
from django.db.models.deletion import CASCADE
# accounts
from account.models import Account

# Create your models here.
class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return str(self.cart_id)
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE,)
    product = models.ForeignKey("store.Product", on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.product
     
    def get_total(self):
        return self.product.price * self.quantity
