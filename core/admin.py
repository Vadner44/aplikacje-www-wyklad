from django.contrib import admin

# Register your models here.
from core.models import BreedingFarm, Bunny


@admin.register(BreedingFarm)
class BreedingFarmAdmin(admin.ModelAdmin):
    pass


@admin.register(Bunny)
class BunnyAdmin(admin.ModelAdmin):
    pass
