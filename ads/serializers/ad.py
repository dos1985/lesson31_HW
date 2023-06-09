from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer, SlugRelatedField
from ads.models import AdModel
from ads.models import CategoryModel
from users.models import User
from validators import not_published


class AdSerializer(ModelSerializer):
    is_published = serializers.BooleanField(validators=[not_published])

    class Meta:
        model = AdModel
        fields = ["author", "category", "name", "price", "description", "is_published"]


# class AdCreateSerializer(serializers.ModelSerializer):
#
#
#     class Meta:
#         model = AdModel
#         fields = ["author", "category", "name", "price", "description", "is_published"]


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
        fields = "__all__"