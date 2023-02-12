from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(("ایمیل"), unique=True)
    first_name_fa = models.CharField(("نام"), max_length=255)    
    last_name_fa = models.CharField(("نام خانوادگی"), max_length=255)

    def __str__(self):
        return f'{self.first_name_fa} {self.last_name_fa}'

    class Meta:
        verbose_name_plural = 'کاربران'
