from django.conf.urls.static import static
from django.urls import path
from rest_framework import routers

from ads.views.category import *
from ads.views.ad import *
from ads.views.selection import SelectionViewSet
from myproject import settings

simple_router = routers.SimpleRouter()
simple_router.register('ad', AdViewSet)
simple_router.register('selection', SelectionViewSet)
simple_router.register('cat', CatViewSet)

urlpatterns = [
    # path('cat/', CategoryView.as_view(), name='cat'),
    # path('cat/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    # path('cat/<int:pk>/update/', CategoryUpdateView.as_view(), name='category-update'),
    # path('cat/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category-delete'),
    # path('cat/create/', CategoryCreateView.as_view()),
    path('ad/<int:pk>/upload_image/', AdImageView.as_view(), name='ad-upload-image'),

]

urlpatterns += simple_router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)