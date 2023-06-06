from datetime import date

from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=100, unique=True)
    lat = models.DecimalField(max_digits=8, decimal_places=6, null=True)
    lng = models.DecimalField(max_digits=8, decimal_places=6, null=True)

    class Meta:
        verbose_name = 'Местположение'
        verbose_name_plural = 'Местположения'

    def __str__(self):
        return self.name


class UserRoles(models.Model):
    MEMBER = 'member'
    MODERATOR = 'moderator'
    ADMIN = 'admin'
    choices = ((MEMBER, 'Пользователь'),
               (MODERATOR, 'Модератор'),
               (ADMIN, 'Администратор'))


def validate_birth_date(value):
    today = date.today()
    age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))
    if age < 9:
        raise ValidationError("Пользователь должен быть старше 9 лет.")


def validate_email_domain(value):
    if value.endswith('@rambler.ru'):
        raise ValidationError("Регистрация с почтового адреса в домене rambler.ru запрещена.")

class User(AbstractUser):
    age = models.PositiveIntegerField()
    location = models.ManyToManyField(Location)
    role = models.CharField(choices=UserRoles.choices, default=UserRoles.MEMBER, max_length=10)
    birth_date = models.DateField(null=True, blank=True, validators=[validate_birth_date])
    email = models.EmailField(blank=True, validators=[validate_email_domain])

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['username']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# class User(models.Model):
#     first_name = models.CharField(verbose_name='Имя', max_length=50, null=True)
#     last_name = models.CharField(verbose_name='Фамилия', max_length=100, null=True)
#     username = models.CharField(verbose_name='Логин', max_length=150, unique=True)
#     password = models.CharField(verbose_name='Пароль', max_length=150)
#     age = models.PositiveIntegerField()
#     location = models.ManyToManyField(Location)
#     role = models.CharField(choices=UserRoles.choices, default=UserRoles.MEMBER, max_length=10)
#     total_ads = models.PositiveIntegerField(default=0)
#
#     class Meta:
#         verbose_name = 'Пользователь'
#         verbose_name_plural = 'Пользователи'
#         ordering = ['username']
#
#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"
