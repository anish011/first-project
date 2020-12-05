from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from authorization import models
from authorization import forms

# Register your models here.
class MyUser(UserAdmin):
    add_form = forms.UserCreateForm
    form = forms.UserUpdateForm
    list_display = ['first_name', 'email',]
    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('birth_date',)}),
    )

admin.site.register(models.UserCreate, MyUser)
