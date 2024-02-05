from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Product, AdvUser

admin.site.register(Product)
admin.site.register(AdvUser)
