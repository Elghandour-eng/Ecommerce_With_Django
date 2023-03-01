from django.contrib import admin
from .models import Category
# Register your models here.

# Category Admin
class CategorAdmin(admin.ModelAdmin):
    prepopulated_fields={'categorySlug':('categoryName',)} # categorySlug will be populated by categoryName
    list_display=('categoryName','categorySlug') # Displaying the fields in the admin
    
    
admin.site.register(Category,CategorAdmin)
