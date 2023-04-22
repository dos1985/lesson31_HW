
import json

import pandas
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from ads.models import CategoryModel
from django.views.generic import DetailView

from ads.models import AdModel


def my_index(request):
    return JsonResponse({"status": "ok"})

@method_decorator(csrf_exempt, name='dispatch')
class CategoryView(View):
    def get(self, request):
        categories = CategoryModel.objects.all()
        response = []
        for category in categories:
            response.append({
                "id": category.id,
                "name": category.name
            })

        return JsonResponse(response, safe=False)


    def post(self, request):

        category_data = json.loads(request.body)
        try:
            category = CategoryModel.objects.get(name=category_data["name"])
            category = CategoryModel.objects.filter(name=category_data["name"]).first()
        except CategoryModel.DoesNotExist:
            return JsonResponse({"message": "Нет такой категории"}, status=404)


        return JsonResponse({
            "id": category.id,
            "name": category.name
        })


class CategoryDetailView(DetailView):
    model = CategoryModel

    def get(self, request, *args, **kwargs):

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

        ads = AdModel.objects.all()

        response = []

        for ad in ads:
            response.append({
                "id": ad.id,
                "name": ad.name,
                "author": ad.author,
                "price": ad.price
            })

        return JsonResponse(response, safe=False)

    def post(self, request):

        ad_data = json.loads(request.body)

        ad = AdModel.objects.create(
            name=ad_data["name"],
            author=ad_data["author"],
            address=ad_data["address"],
            description=ad_data["description"],
            price=ad_data["price"],
            is_published=ad_data["is_published"]
        )

        return JsonResponse({
            "id": ad.id,
            "name": ad.name,
            "author": ad.author,
            "address": ad.address,
            "description": ad.description,
            "price": ad.price,
            "is_published": ad.is_published
        })


class AdDetailView(DetailView):
    model = AdModel

    def get(self, request, *args, **kwargs):

        try:
            ad = self.get_object()
        except AdModel.DoesNotExist:
            return JsonResponse({"error": "Not found"}, status=404)

        return JsonResponse({
            "id": ad.id,
            "name": ad.name,
            "author": ad.author,
            "address": ad.address,
            "description": ad.description,
            "price": ad.price,
            "is_published": ad.is_published
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