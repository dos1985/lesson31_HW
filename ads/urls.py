from django.conf.urls.static import static
from django.urls import path

from myproject import settings
from . import views
from .views import AdView, CategoryDetailView, AdDetailView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView, \
    AdUpdateView, AdDeleteView, AdImageView
urlpatterns = [
    path("", views.my_index, name="index"),
    path('cat/', views.CategoryView.as_view(), name='cat'),
    path('cat/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('cat/<int:pk>/update/', CategoryUpdateView.as_view(), name='category-update'),
    path('cat/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category-delete'),
    path('cat/create/', views.CategoryCreateView.as_view()),
    path('ad/', AdView.as_view(), name='ad_all'),
    path('ad/<int:pk>/', AdDetailView.as_view(), name='cat-detail'),
    path('ad/<int:pk>/update/', AdUpdateView.as_view(), name='cat-update'),
    path('ad/<int:pk>/delete/', AdDeleteView.as_view(), name='cat-delete'),
    path('ad/<int:pk>/upload_image/', AdImageView.as_view(), name='ad-upload-image'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)