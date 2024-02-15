from django import forms
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, BaseUserManager
)


class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Email address is required')
        if not username:
            raise ValueError('Username is required')
        
        email = self.normalize_email(email)
        user = self.model(
            username=username,
            email=email,  
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        super_user = self.create_user(email, username, password)
        super_user.is_staff = True
        super_user.is_superuser = True
        super_user.save(using=self._db)
        return super_user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        max_length=250, unique=True,
        verbose_name='email address'
    )
    username = models.CharField(max_length=100, verbose_name='username')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username