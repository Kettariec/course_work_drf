from django.db import models
from django.contrib.auth.models import AbstractUser

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='почта пользователя')
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    city = models.CharField(max_length=35, verbose_name='город', **NULLABLE)
    avatar = models.ImageField(upload_to='users/',
                               verbose_name='аватар', **NULLABLE)
    telegram_id = models.BigIntegerField(default=0, verbose_name='телеграмм id')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
