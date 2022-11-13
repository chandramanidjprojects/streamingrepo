from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from . forms import UserAdminCreationForm,UserAdminChangeForm
from . models import Post,Comment
class CreateUserAdmin(UserAdmin):
    add_form=UserAdminCreationForm
    form=UserAdminChangeForm
    list_display=['id','email','staff']
    list_filter=['active','staff','admin']
    fieldsets=(
        ('contact',{'fields':('email','password',)}),
        ('Personal',{'fields':('username','profile')}),
        ('Permissions',{'fields':('admin','active','staff')})
    )
    add_fieldsets=(
        ('register',{'classes':('wide',),
                'fields':('email','password1','password2',)      
              }
        ),
        
    )
    ordering=('email',)
    filter_horizontal=()
admin.site.register(get_user_model(),CreateUserAdmin)
admin.site.register(Post)
admin.site.register(Comment)