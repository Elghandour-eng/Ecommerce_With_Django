from django.db import models
from category.models import Category
from django.urls import reverse # Used to generate URLs by reversing the URL patterns

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length =100,unique=True)
    product_slug = models.SlugField(max_length =100)
    product_description = models.TextField(max_length =400,blank=True) # blank=True means that the field is not required
    product_price = models.IntegerField()
    product_stock = models.IntegerField()
    product_isavilabe = models.BooleanField(default=True)
    product_image =models.ImageField(upload_to='photos/products')
    product_category = models.ForeignKey(Category,on_delete=models.CASCADE) # on_delete=models.CASCADE means that if the category is deleted, the product will be deleted too
    created_date = models.DateTimeField(auto_now_add=True) # auto_now_add=True means that the date will be added automatically
    modified_date = models.DateTimeField(auto_now = True)  # auto_now=True means that the date will be updated automatically
    #created_by = models.ForeignKey('account.Account',on_delete=models.CASCADE,related_name='product_created_by',null=True,blank=True,) 
    
    def get_url(self):
        return reverse("product_details", args = [self.product_category.categorySlug,self.product_slug])
    
    def __str__(self) -> str :
        return self.product_name
    
    
  