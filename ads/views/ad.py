from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from ads.models import AdModel
from ads.serializers.ad import AdDetailSerializer, AdListSerializer, AdSerializer


class AdViewSet(ModelViewSet):
    queryset = AdModel.objects.order_by('-price')
    serializer_class = AdSerializer
    serializers_classes = {
        "retrieve": AdDetailSerializer,
        "list": AdListSerializer
    }

    default_permission = [AllowAny()]
    permissions = {"retrieve": [IsAuthenticated()]}

    def get_permissions(self):
        return self.permissions.get(self.action, self.default_permission)

    def get_serializer_class(self):
        return self.serializers_classes.get(self.action, self.serializer_class)

    def list(self, request, *args, **kwargs):
        categories = request.GET.getlist('cat')
        if categories:
            self.queryset = self.queryset.filter(category_id__in=categories)
        text = request.GET.get('text')
        if text:
            self.queryset = self.queryset.filter(name__icontains=text)

        location = request.GET.get('location')
        if location:
            self.queryset = self.queryset.filter(author__location__name__icontains=location)


        price_from = request.GET.get('price_from')
        price_to = request.GET.get('price_to')
        if price_to:
            self.queryset = self.queryset.filter(price__lte=price_to)
        if price_from:
            self.queryset = self.queryset.filter(price__gte=price_from)
        return super().list(self, request, *args, **kwargs)





@method_decorator(csrf_exempt, name='dispatch')
class AdImageView(UpdateView):
    model = AdModel
    fields = ["image"]

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        self.object.image = request.FILES.get("image", None)
        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name,
            "author": self.object.author.username,
            "price": self.object.price,
            "description": self.object.description,
            "image": self.object.image.url if self.object.image else None
        })


