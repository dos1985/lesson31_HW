from rest_framework import serializers

from ads.models import AdModel


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdModel
        fields = '__all__'