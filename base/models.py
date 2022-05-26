from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import CharField
from .manager import UserManager

# Create your models here.
class User(AbstractUser):
    username=None
    first_name=models.CharField(null=True, max_length=11, default="x")
    last_name=models.CharField(null=True, max_length=11, default="x")
    email=models.EmailField(unique=True, null=False)
    phone_no=models.CharField(max_length=11, null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'email'
    objects=UserManager()
    REQUIRED_FIELDS=[]

