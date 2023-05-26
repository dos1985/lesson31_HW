import json
import pandas
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from ads.models import CategoryModel
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView






@method_decorator(csrf_exempt, name='dispatch')
class CategoryView(View):

    def get(self, request):
        """Получаем все данные из категории"""
        categories = CategoryModel.objects.all().order_by('name')
        response = []
        for category in categories:
            response.append({
                "id": category.id,
                "name": category.name
            })

        return JsonResponse(response, safe=False)


    def post(self, request):
        """Пойск категории по имени"""
        category_data = json.loads(request.body)
        category_name = category_data["name"].lower()

        try:
            category = CategoryModel.objects.get(name__iexact=category_name)
        except CategoryModel.DoesNotExist:
            return JsonResponse({"message": "Нет такой категории"}, status=404)

        return JsonResponse({
            "id": category.id,
            "name": category.name
        })


@method_decorator(csrf_exempt, name='dispatch')
class CategoryCreateView(CreateView):
    """Создаем категорию"""
    model = CategoryModel
    fields = ["name"]

    def post(self, request, *args, **kwargs):
        category_data = json.loads(request.body)

        category = CategoryModel.objects.create(
            name=category_data["name"]
        )

        return JsonResponse({
            "id": category.id,
            "name": category.name
        })


@method_decorator(csrf_exempt, name='dispatch')
class CategoryUpdateView(UpdateView):
    """Обновляем категорию"""
    model = CategoryModel
    fields = ["name"]

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        category_data = json.loads(request.body)

        self.object.name = category_data["name"]
        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name
        })


@method_decorator(csrf_exempt, name='dispatch')
class CategoryDeleteView(DeleteView):
    """Удаляем категорию"""
    model = CategoryModel
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        return JsonResponse({"status": "ok"}, status=200)


class CategoryDetailView(DetailView):
    model = CategoryModel

    def get(self, request, *args, **kwargs):
        """Получаем данные из категории по id"""
        try:
            category = self.get_object()
        except CategoryModel.DoesNotExist:
            return JsonResponse({"error": "Not found"}, status=404)

        return JsonResponse({
            "id": category.id,
            "name": category.name
        })



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

