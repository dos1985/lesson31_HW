from django.contrib import admin

from ads.models import AdModel, CategoryModel
from users.models import Location, User

admin.site.register(User)
admin.site.register(Location)
