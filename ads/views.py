
import json

import pandas
from category import Category
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from ads.models import CategoryModel
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from ads.models import AdModel
from users.models import User


def my_index(request):
    return JsonResponse({"status": "ok"})


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


@method_decorator(csrf_exempt, name='dispatch')
class AdView(View):
    def get(self, request):
        """Получаем все объявления"""
        ads = AdModel.objects.all()
        paginator = Paginator(ads, 10)  # каждая страница содержит 10 элементов
        page_num = request.GET.get('page') or 1
        page = paginator.get_page(page_num)
        items = []
        for ad in page.object_list:
            items.append({
                "id": ad.id,
                "name": ad.name,
                "author_id": ad.author.id,
                "author": str(ad.author),
                "price": ad.price,
                "description": ad.description,
                "is_published": ad.is_published,
                "category_id": ad.category.id,
                "image": str(ad.image),
            })
        response = {
            "items": items,
            "total": paginator.count,
            "num_pages": paginator.num_pages,
        }
        return JsonResponse(response, safe=False)

    def get_queryset(self):
        return self.model.objects.order_by('-price')


    def post(self, request):
        """Поиск объявления по имени"""
        ad_data = json.loads(request.body)
        author_name = ad_data.get("author")
        try:
            author = User.objects.get(username__iexact=author_name)
        except ObjectDoesNotExist:
            return JsonResponse({"error": "User with username {} does not exist".format(author_name)}, status=400)

        ad = AdModel.objects.create(
            name=ad_data["name"],
            author=author,
            address=ad_data["address"],
            description=ad_data["description"],
            price=ad_data["price"],
            is_published=ad_data["is_published"]
        )

        return JsonResponse({
            "id": ad.id,
            "name": ad.name,
            "author": ad.author.username,
            "address": ad.address,
            "description": ad.description,
            "price": ad.price,
            "is_published": ad.is_published
        })


class AdDetailView(DetailView):
    """Получаем данные из объявления по id"""
    model = AdModel

    def get(self, request, *args, **kwargs):

        try:
            ad = self.get_object()
        except AdModel.DoesNotExist:
            return JsonResponse({"error": "Not found"}, status=404)

        return JsonResponse({
            "id": ad.id,
            "name": ad.name,
            "author": str(ad.author),
            "description": ad.description,
            "price": ad.price,
            "is_published": ad.is_published
        })


@method_decorator(csrf_exempt, name='dispatch')
class AdUpdateView(UpdateView):
    """Обновляем объявление"""
    model = AdModel
    fields = ["name", "author", "description", "price", "is_published"]

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        ad_data = json.loads(request.body)

        self.object.name = ad_data["name"]
        self.object.author_id = ad_data["author_id"]
        self.object.description = ad_data["description"]
        self.object.price = ad_data["price"]
        self.object.is_published = ad_data["category_id"]
        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name,
            "author": str(self.object.author),
            "description": self.object.description,
            "price": self.object.price,
            "is_published": self.object.is_published
        })


@method_decorator(csrf_exempt, name='dispatch')
class AdDeleteView(DeleteView):
    """Удаляем объявление"""
    model = AdModel
    success_url = "/"
    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        return JsonResponse({"status": "ok"}, status=200)


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


class AddToAd(View):
    def get(self, request):
        csv_data = pandas.read_csv('ads/data/ads.csv', sep=",").to_dict()
        i = 0
        while max(csv_data['Id'].keys()) >= i:
            AdModel.objects.create(
                name=csv_data["name"][i],
                author=csv_data["author"][i],
                price=csv_data["price"][i],
                description=csv_data["description"][i],
                address=csv_data["address"][i],
                is_published=csv_data["is_published"][i],
            )
            i += 1
        return JsonResponse("Added to table Ads", safe=False, status=200)