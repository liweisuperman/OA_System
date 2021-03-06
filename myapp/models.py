from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class MyUser(AbstractUser):
    phone = models.CharField(
        max_length=13,
        unique=True,
        verbose_name="手机号"
    )
    email = models.EmailField(
        null=True
    )
    persimission = models.IntegerField(
        default=1
    )
    create_time = models.DateTimeField(
        auto_now_add=True
    )



