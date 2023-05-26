from django.conf.urls.static import static
from django.urls import path
from rest_framework import routers

from ads.views.category import *
from ads.views.ad import *
from myproject import settings

simple_router = routers.SimpleRouter()
simple_router.register('ad', AdViewSet)

urlpatterns = [
    path('cat/', CategoryView.as_view(), name='cat'),
    path('cat/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('cat/<int:pk>/update/', CategoryUpdateView.as_view(), name='category-update'),
    path('cat/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category-delete'),
    path('cat/create/', CategoryCreateView.as_view()),
    # path('ad/', AdView.as_view(), name='ad_all'),
    # path('ad/<int:pk>/', AdDetailView.as_view(), name='cat-detail'),
    # path('ad/<int:pk>/update/', AdUpdateView.as_view(), name='cat-update'),
    # path('ad/<int:pk>/delete/', AdDeleteView.as_view(), name='cat-delete'),
    path('ad/<int:pk>/upload_image/', AdImageView.as_view(), name='ad-upload-image'),

]

urlpatterns += simple_router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)