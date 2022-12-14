# Generated by Django 4.1.2 on 2022-10-26 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        max_length=255, unique=True, verbose_name="Имя пользователя"
                    ),
                ),
                (
                    "password_hash",
                    models.CharField(max_length=255, verbose_name="Хэш пароля"),
                ),
                (
                    "password_salt",
                    models.CharField(max_length=255, verbose_name="Соль пароля"),
                ),
            ],
        ),
    ]
