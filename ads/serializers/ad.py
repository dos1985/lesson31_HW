from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer, SlugRelatedField

from ads.models import AdModel
from ads.models import CategoryModel
from users.models import User


class AdSerializer(ModelSerializer):
    class Meta:
        model = AdModel
        fields = "__all__"


class AdDetailSerializer(ModelSerializer):
    author = SlugRelatedField(slug_field="username", queryset=User.objects.all())
    category = SlugRelatedField(slug_field="name", queryset=CategoryModel.objects.all())
    locations = SerializerMethodField()

    def get_locations(self, ad):
        return [location.name for location in ad.author.location.all()]

    class Meta:
        model = AdModel
        fields = "__all__"


class AdListSerializer(ModelSerializer):
    author = SlugRelatedField(slug_field="username", queryset=User.objects.all())
    category = SlugRelatedField(slug_field="name", queryset=CategoryModel.objects.all())

    class Meta:
        model = AdModel
        fields = ["id", "name", "author", "category", "price"]