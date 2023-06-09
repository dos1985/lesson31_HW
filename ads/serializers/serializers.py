from rest_framework import serializers
from rest_framework.response import Response
from ads.models import AdModel, Selection, CategoryModel



class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdModel
        fields = '__all__'



class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = "__all__"


class SelectionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        fields = ["id", "name"]


class SelectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        fields = "__all__"


class SelectionDetailSerializer(serializers.ModelSerializer):
    items = AdSerializer(many=True)

    class Meta:
        model = Selection
        fields = "__all__"