from django.urls import path

from .views import UserView, UserDetailView, UserCreateView, UserUpdateView, UserDeleteView, UserZView

urlpatterns = [
    path('users/', UserView.as_view(), name='users'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='users-detail'),
    path('users/create/', UserCreateView.as_view(), name='users-create'),
    path('users/<int:pk>/update/', UserUpdateView.as_view(), name='users-update'),
    path('users/<int:pk>/delete/', UserDeleteView.as_view(), name='users-delete'),
    path('users/Z/', UserZView.as_view(), name='users-Z'),

]