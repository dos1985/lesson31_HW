from django.contrib.auth.models import AbstractUser
from django.db import models
from users.validators import validate_birth_date, validate_email_domain


class Location(models.Model):
    name = models.CharField(max_length=100)
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

class User(AbstractUser):
    age = models.PositiveIntegerField()
    location = models.ManyToManyField(Location)
    role = models.CharField(choices=UserRoles.choices, default=UserRoles.MEMBER, max_length=10)
    birth_date = models.DateField(blank=True, validators=[validate_birth_date], null=True)
    email = models.EmailField(blank=True, validators=[validate_email_domain])

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['username']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

