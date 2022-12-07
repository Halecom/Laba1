from django.db import models


class User(models.Model):
    username = models.CharField(max_length=255, unique=True, verbose_name="Имя пользователя")
    password_hash = models.CharField(max_length=255, verbose_name="Хэш пароля")
    password_salt = models.CharField(max_length=255, verbose_name="Соль пароля")
