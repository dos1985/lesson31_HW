from django.db import router
from django.urls import path, include
from requests import delete
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.views import UserUpdateView, UserListAPIView, UserCreateView, LocationViewSet, UserDestroyAPIView, \
    UserDetailView

simple_router = routers.SimpleRouter()
simple_router.register('location', LocationViewSet)

urlpatterns = [
    # path('', include(simple_router.urls)),
    path('users/', UserListAPIView.as_view()),
    path('users/<int:pk>/', UserDetailView.as_view()),
    path('users/create/', UserCreateView.as_view()),
    path('users/<int:pk>/update/', UserUpdateView.as_view(), name='users-update'),
    path('users/<int:pk>/', UserDestroyAPIView.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),


]

urlpatterns += simple_router.urls

