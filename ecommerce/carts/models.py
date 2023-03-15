from django.db import models
from django.db.models.deletion import CASCADE
# accounts
from account.models import Account

# Create your models here.
class Cart(models.Model):
    id = models.AutoField(primary_key=True, blank=False, null=False)
    user = models.ForeignKey("account.Account", on_delete=models.CASCADE, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return str(self.id)
    
class CartItem(models.Model):
    id = models.AutoField(primary_key=True, blank=False, null=False)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, blank=False, null=False)
    product = models.ForeignKey("store.Product", on_delete=models.CASCADE, blank=False, null=False)
    quantity = models.IntegerField(default=1)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.id)
    
    def get_total(self):
        return self.product.price * self.quantity
