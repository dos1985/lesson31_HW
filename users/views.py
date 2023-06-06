
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, \
DestroyAPIView
from rest_framework.viewsets import ModelViewSet

from users.models import User, Location
from users.serializers import UserSerializer, UserDestroySerializer, \
    LocationSerializer, UserCreateUpdateSerializer


class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserUpdateView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateUpdateSerializer


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateUpdateSerializer


class UserDestroyAPIView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDestroySerializer


class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
