from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from authorization import models


class UserCreateForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = models.UserCreate
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'birth_date')


class UserUpdateForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = models.UserCreate
        fields = ('username', 'first_name', 'last_name', 'birth_date')
