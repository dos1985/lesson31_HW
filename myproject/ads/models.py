import json

from django.db import models


class AdModel(models.Model):
    name = models.CharField(max_length=50, unique=True)
    author = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    description = models.TextField(max_length=500, null=True)
    address = models.CharField(max_length=250)
    is_published = models.BooleanField(default=True)


class CategoryModel(models.Model):
    name = models.CharField(max_length=100, unique=True)

# def load_data_from_json_file(file_path):
#     with open(file_path, 'r') as json_file:
#         data = json.load(json_file)
#         for item in data:
#             category = CategoryModel(name=item['name'])
#             category.save()
#
# json_path = r"/myproject/data\categories.json"
# load_data_from_json_file(json_path)
