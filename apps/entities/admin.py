from django.contrib import admin
from .models import Origin, Villain, Category, Entity


# Register your models here.
@admin.register(Origin)
class OriginAdmin(admin.ModelAdmin):
    actions_selection_counter = True
    list_display = ("name", "hero_count", "villain_count")
    prepopulated_fields = {
        "name": ("name",),
    }

    def hero_count(self, obj: Origin):
        return obj._hero_count

    def villain_count(self, obj: Origin):
        return obj._villain_count


class VillainInline(admin.StackedInline):
    model = Villain
    extra = 0


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [VillainInline]
    search_fields = ("name",)


@admin.register(Villain)
class VillainAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "origin",
        "is_immortal",
        "malevolence_factor",
        "power_factor",
        "is_unique",
        "count",
    )
    prepopulated_fields = {
        "name": ("category", "name"),
    }
    autocomplete_fields = ("category",)
    save_on_top = True
