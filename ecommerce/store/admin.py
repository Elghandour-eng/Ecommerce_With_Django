from django.contrib import admin
from .models import Product 

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display=('product_name','product_price','product_stock','product_isavilabe','product_category','created_date','modified_date')
    prepopulated_fields={'product_slug':('product_name',)}
    list_per_page=20


admin.site.register(Product,ProductAdmin)
