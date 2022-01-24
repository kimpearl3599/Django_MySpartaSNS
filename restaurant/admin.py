from django.contrib import admin
from .models import MyTopping, MyPizza


admin.site.register(MyPizza)
admin.site.register(MyTopping)
