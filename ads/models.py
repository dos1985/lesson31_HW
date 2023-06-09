import json

from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator
from django.db import models
from django.utils.text import slugify

from users.models import User


class CategoryModel(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.CharField(max_length=10, unique=True, validators=[MinLengthValidator(5), MaxLengthValidator(10)])


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)[:10]
        super(CategoryModel, self).save(*args, **kwargs)



class AdModel(models.Model):
    name = models.CharField(max_length=50, null=False, validators=[MinLengthValidator(10)])
    author = models.ForeignKey(User, verbose_name='Автор', related_name='ads', on_delete=models.CASCADE)
    price = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    description = models.CharField(max_length=500, null=True, blank=True)
    is_published = models.BooleanField(default=False)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='pictures', null=True, blank=True)

    # def save(self, *args, **kwargs):
    #     if self.is_published and not self.pk:
    #         raise ValidationError("Значение поля is_published при создании объявления не может быть True.")
    #     super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return self.name

class Selection(models.Model):
    name = models.CharField(max_length=100, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Владелец")
    items = models.ManyToManyField(AdModel)



    class Meta:
        verbose_name = 'Подборка'
        verbose_name_plural = 'Подборки'

    def __str__(self):
        return self.name



