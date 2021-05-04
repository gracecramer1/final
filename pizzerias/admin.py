from django.contrib import admin

# Register your models here.

from .models import Name, Topping

admin.site.register(Name)
admin.site.register(Topping)
