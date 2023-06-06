import json
import pandas
from django.http import JsonResponse
from django.views import View
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from ads.models import CategoryModel
from ads.serializers.serializers import CatSerializer


class CatViewSet(ModelViewSet):
    queryset = CategoryModel.objects.all()
    serializer_class = CatSerializer

    def list(self, request, *args, **kwargs):
        cat_name = request.GET.get("name", None)
        if cat_name:
            try:
                queryset = self.queryset.filter(name__iexact=cat_name)
                if not queryset.exists():
                    return Response({"message": "Нет такой категории"}, status=404)
            except CategoryModel.DoesNotExist:
                return Response({"message": "Нет такой категории"}, status=404)
        else:
            queryset = self.queryset.all()

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)




class AddToCat(View):
    def get(self, request):
        csv_data = pandas.read_csv('ads/data/categories.csv', sep=",").to_dict()
        i = 0
        while max(csv_data['id'].keys()) >= i:
            CategoryModel.objects.create(
                name=csv_data["name"][i],
            )
            i += 1
        return JsonResponse("Added to table Category", safe=False, status=200)

