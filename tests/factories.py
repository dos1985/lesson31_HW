import factory

from ads.models import AdModel
from ads.models import CategoryModel
from users.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("name")
    birth_date = "2010-03-05"


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CategoryModel

    name = factory.Faker("name")
    slug = factory.Faker("ean", length=8)


class AdFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = AdModel

    name = factory.Faker("name")
    category = factory.SubFactory(CategoryFactory)
    author = factory.SubFactory(UserFactory)
    price = 200