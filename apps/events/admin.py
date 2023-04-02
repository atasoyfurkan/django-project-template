from django.contrib import admin
from .models import Epic, Event, EventHero, EventVillain


# Register your models here.
@admin.register(Epic)
class EpicAdmin(admin.ModelAdmin):
    filter_horizontal = ("participating_heroes", "participating_villains")
