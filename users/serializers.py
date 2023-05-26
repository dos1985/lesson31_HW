
from rest_framework import serializers, status
from users.models import User, Location


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'name']

    # def to_representation(self, instance):
    #     return instance.name


class UserSerializer(serializers.ModelSerializer):
    location = LocationSerializer(many=True, read_only=True)
    locations = serializers.SlugRelatedField(
        required=False,
        many=True,
        queryset=Location.objects.all(),
        slug_field="name"
    )

    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "role", "age", "location", "locations"]


class UserUpdateSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(
        required=False,
        many=True,
        queryset=Location.objects.all(),
        slug_field="name"
    )

    def is_valid(self, raise_exception=False):
        self._location = self.initial_data.pop("location")
        return super().is_valid(raise_exception=raise_exception)

    def save(self):
        user = super().save()

        # Очищаем все существующие местоположения пользователя
        user.location.clear()

        # Добавляем новые местоположения
        for location_name in self._location:
            location_obj, _ = Location.objects.get_or_create(name=location_name)
            user.location.add(location_obj)

        # Сохраняем объект сериализатора
        self.instance = user

        return user

    class Meta:
        model = User
        fields = '__all__'

class UserCreateSerializer(serializers.ModelSerializer):
    location = serializers.SlugRelatedField(
        required=False,
        many=True,
        queryset=Location.objects.all(),
        slug_field="name",
    )

    def is_valid(self, raise_exception=False):
        self._locations = self.initial_data.pop("location", [])
        return super().is_valid(raise_exception=raise_exception)

    def create(self, validated_data):

        user = User.objects.create(**validated_data)

        for location_name in self._locations:
            location, _ = Location.objects.get_or_create(name=location_name)
            user.location.add(location)
        return user

    class Meta:
        model = User
        fields = "__all__"


class UserDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"





