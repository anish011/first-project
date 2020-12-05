from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.
class UserCreateManager(BaseUserManager):
    def _create_user(self, username, email, first_name, is_staff, is_superuser, password, **kwargs):
        if not username:
            raise ValueError('Username is mandatory')
        if not email:
            raise ValueError('Email is mandatory')
        email = self.normalize_email(email)
        if not first_name:
            raise ValueError('First Name is mandatory')
        user = self.model(username=username, email=email, first_name=first_name, is_staff=is_staff,
                            is_superuser=is_superuser, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, first_name, password=None, **kwargs):
        return self._create_user(username, email, first_name, False, False, password, **kwargs)

    def create_superuser(self, username, email, first_name, password=None, **kwargs):
        return self._create_user(username, email, first_name, True, True, password, **kwargs)


class UserCreate(AbstractUser):
    object = UserCreateManager()
    username = models.CharField(unique=True, max_length=10)
    email = models.EmailField(unique=True)
    birth_date = models.DateField(blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name',]
