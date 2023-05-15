import json

from django.db import models

from users.models import User


class CategoryModel(models.Model):
    name = models.CharField(max_length=100, unique=True)


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name



class AdModel(models.Model):
    name = models.CharField(max_length=50, unique=True)
    author = models.ForeignKey(User, verbose_name='Автор', related_name='ads', on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    description = models.TextField(max_length=500, null=True)
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='pictures', null=True, blank=True)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return self.name



