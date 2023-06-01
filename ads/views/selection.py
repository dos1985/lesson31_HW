from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from ads.models import Selection
from ads.permissions import IsOwnerSelection
from ads.serializers.serializers import SelectionDetailSerializer, SelectionListSerializer, SelectionSerializer


class SelectionViewSet(ModelViewSet):
    queryset = Selection.objects.all()

    serializer_class = SelectionSerializer
    serializers_classes = {
        "list": SelectionListSerializer,
        "retrieve": SelectionDetailSerializer
    }

    default_permission = [AllowAny()]
    permissions = {
        "create": [IsAuthenticated()],
        "update": [IsAuthenticated(), IsOwnerSelection()],
        "partial_update": [IsAuthenticated(), IsOwnerSelection()],
        "destroy": [IsAuthenticated(), IsOwnerSelection()]
    }

    def get_permissions(self):
        return self.permissions.get(self.action, self.default_permission)

    def get_serializer_class(self):
        return self.serializers_classes.get(self.action, self.serializer_class)