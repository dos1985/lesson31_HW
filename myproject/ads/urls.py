
from django.urls import path, include
from . import views
from .views import AdView, CategoryDetailView, AdDetailView, CategoryView

urlpatterns = [
    path("", views.my_index, name="index"),
    path('cat/', views.CategoryView.as_view(), name='cat'),
    path('cat/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('ad/', name='ad', view=AdView.as_view()),
    path('ad/<int:pk>/', AdDetailView.as_view(), name='cat-detail')


    ]
