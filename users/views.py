import json

from django.core import paginator
from django.core.paginator import Paginator
from django.http import JsonResponse, HttpResponseServerError
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from httpretty import Response
from rest_framework import generics, filters, status
from rest_framework.pagination import PageNumberPagination
from users.models import User, Location
from users.serializers import UserSerializer


@method_decorator(csrf_exempt, name='dispatch')
class UserView(View):
    def get(self, request):
        """Получение списка пользователей"""
        try:
            users = User.objects.all()
            response = []
            for user in users:
                locations = ", ".join([location.name for location in user.location.all()])
                response.append({
                    "id": user.id,
                    "username": user.username,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "role": user.role,
                    "age": user.age,
                    "location": locations,
                })
            return JsonResponse(response, safe=False)
        except Exception as e:
            return HttpResponseServerError(str(e))


@method_decorator(csrf_exempt, name='dispatch')
class UserZView(View):
    def get(self, request):
        users = User.objects.all()
        paginator = Paginator(users, 10)  # каждая страница содержит 10 элементов
        page_num = request.GET.get('page') or 1
        page = paginator.get_page(page_num)
        items = []
        for user in page.object_list:
            items.append({
                "id": user.id,
                "username": user.username,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "role": user.role,
                "age": user.age,
                "location": user.location.name,  # поле name из location
                "total_ads": user.ads.count(),
            })
        response = {
            "items": items,
            "total": paginator.count,
            "per_page": paginator.per_page,
        }
        return JsonResponse(response, status=status.HTTP_200_OK)


class UserDetailView(DetailView):
    """Получение пользователя по pk"""
    model = User

    def get(self, request, *args, **kwargs):
        try:
            user = self.get_object()
        except User.DoesNotExist:
            return JsonResponse({"message": "Пользователь не найден"}, status=404)

        return JsonResponse({
            "id": user.id,
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "role": user.role,
            "age": user.age,
            "location": user.location.first().name,
        })



@method_decorator(csrf_exempt, name='dispatch')
class UserCreateView(CreateView):
    """Создание пользователя"""
    model = User
    fields = ["username", "first_name", "last_name", "role", "age", "location"]

    def post(self, request, *args, **kwargs):
        user_data = json.loads(request.body)

        user = User.objects.create(
            username=user_data["username"],
            first_name=user_data["first_name"],
            last_name=user_data["last_name"],
            role=user_data["role"],
            age=user_data["age"],
        )

        locations = []
        for location_name in user_data["locations"]:
            location, _ = Location.objects.get_or_create(name=location_name)
            locations.append(location)

        user.location.set(locations)

        return JsonResponse({
            "id": user.id,
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "role": user.role,
            "age": user.age,
            "location": [location.name for location in user.location.all()],
        })



@method_decorator(csrf_exempt, name='dispatch')
class UserUpdateView(UpdateView):
    model = User
    fields = ["username", "first_name", "last_name", "role", "age", "location"]

    def post(self, request, *args, **kwargs):
        user_data = json.loads(request.body)
        location = user_data.pop('location', None)

        response = super().post(request, *args, **kwargs)

        if location:
            location_obj, created = Location.objects.get_or_create(name=location)
            self.object.location.clear()
            self.object.location.add(location_obj)

        data = {
            "id": self.object.id,
            "username": self.object.username,
            "first_name": self.object.first_name,
            "last_name": self.object.last_name,
            "role": self.object.role,
            "age": self.object.age,
            "location": self.object.location.first().name if self.object.location.exists() else None,
        }

        return JsonResponse(data)



@method_decorator(csrf_exempt, name='dispatch')
class UserDeleteView(DeleteView):
    """Удаляем Пользователя"""
    model = User
    success_url = "/"
    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        return JsonResponse({"status": "ok"}, status=200)