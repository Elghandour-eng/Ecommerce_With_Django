from django.db import models
#get user model and user manager
from django.contrib.auth.models import AbstractUser , BaseUserManager
#abstract user is used to create a custom user model 
#base user manager is used to create a custom user manager
# Create your models here.

class MyAccountManager(BaseUserManager):
    #this is for creating a user
    def create_user(self,first_name,last_name,username,email,phone_number,password=None):
        if not email:
            raise ValueError("Email is required")
        if not username:
            raise ValueError("User name is required")
        if not first_name:
            raise ValueError("First name is required")
        if not last_name:
            raise ValueError("Last name is required")
        if not phone_number:
            raise ValueError("Phone number is required")

        user=self.model(
            email=self.normalize_email(email), #normalize email is used to convert email to lowercase
            username=username,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
        )

        user.set_password(password)
        user.save(using=self._db) #this is for multiple database
        
        return user
    
    #this is for creating a superuser
    def create_superuser(self,first_name,last_name,username,email,phone_number,password):
      
        
        user=self.create_user(
            email=self.normalize_email(email), #normalize email is used to convert email to lowercase
            username=username,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            password=password,
        )

        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True
        user.is_active=True
        user.is_verified=True
        
        user.save(using=self._db) #this is for multiple database
        return user
        
class Account(AbstractUser):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    username=models.CharField(max_length=50,unique=True)
    email=models.EmailField(max_length=100,unique=True)
    phone_number=models.CharField(max_length=50)
    
    #required fields
    date_joined=models.DateTimeField(auto_now_add=True)
    last_login=models.DateTimeField(auto_now=True)
    is_admin=models.BooleanField(default=False)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    is_verified=models.BooleanField(default=False)
    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username','first_name','last_name','phone_number']
    
    object = MyAccountManager() #this is for creating a user
    
     
    def __str__(self):
        return self.email
    
    
    #this is for admin panel
    def has_perm(self,perm,obj=None):
        return self.is_admin
    
    
    #this is for admin panel
    def has_module_perms(self,app_label):
        #app_label is the name of the app in admin panel
        return True
    
    def get_full_name(self):
        return self.first_name+" "+self.last_name
    
    def get_short_name(self):
        return self.first_name
    
    def get_username(self):
        return self.username
    
    
    
    
    
    
    class Meta:
        verbose_name_plural='Users'
        verbose_name='User'