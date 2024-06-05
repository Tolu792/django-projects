from django.contrib import admin
from .models import Drink


# Register your models here.
class DrinkAdmin(admin.ModelAdmin):
    list_display = ("name", "description")


admin.site.register(Drink, DrinkAdmin)
