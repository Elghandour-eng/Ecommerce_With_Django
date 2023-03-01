from django.db import models

# Create your models here.

# Category Model
class Category(models.Model):
    
    # Category Fields 
    categoryName=models.CharField(max_length=50,unique=True) #Category Name {Unique=True}
    categorySlug=models.SlugField(max_length=50,unique=True) #Category Slug {Unique=True}
    categoryDescription=models.TextField(max_length=200,blank=True) #Category Description
    categoryImage=models.ImageField(upload_to='photos/categories',blank=True) #Category Image
    
    # Meta Class
    class Meta:
        verbose_name="Category" # Verbose Name is a single object to be displayed in the admin
        verbose_name_plural="Categories" # Verbose Name Plural is a plural object to be displayed in the admin
    
    # default ordering
    def __str__(self):
        return self.categoryName
    
