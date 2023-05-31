from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer, SlugRelatedField

from ads.models.ad import Ad
from ads.models.category import Category
from users.models import User


class AdSerializer(ModelSerializer):
    class Meta:
        model = Ad
        fields = "__all__"


class AdDetailSerializer(ModelSerializer):
    author = SlugRelatedField(slug_field="username", queryset=User.objects.all())
    category = SlugRelatedField(slug_field="name", queryset=Category.objects.all())
    locations = SerializerMethodField()

    def get_locations(self, ad):
        return [location.name for location in ad.author.locations.all()]

    class Meta:
        model = Ad
        fields = "__all__"


class AdListSerializer(ModelSerializer):
    author = SlugRelatedField(slug_field="username", queryset=User.objects.all())
    category = SlugRelatedField(slug_field="name", queryset=Category.objects.all())

    class Meta:
        model = Ad
        fields = ["id", "name", "author", "category", "price"]