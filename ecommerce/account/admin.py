from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin



# Register your models here.
class AccountAdmin(UserAdmin):
    list_display=('email','username','first_name','last_name','phone_number','date_joined','last_login','is_admin','is_staff','is_active','is_verified')
    list_display_links=('email','username','first_name','last_name','phone_number') #this is used to make the fields clickable
    search_fields=('email','username','first_name','last_name','phone_number')
    readonly_fields=('date_joined','last_login')
    filter_horizontal=()
    list_filter=()
    fieldsets=()
    ordering=('email','username','first_name','last_name','phone_number','date_joined','last_login','is_admin','is_staff','is_active','is_verified')

    add_fieldsets=(
        (None,{
            'classes':('wide',),
            'fields':('email','username','first_name','last_name','phone_number','password1','password2')
        }),
        # fieldss are used to add fields in the admin
    )

# Register your models here.
admin.site.register(Account,AccountAdmin)
