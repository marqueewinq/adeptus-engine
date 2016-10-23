from django.contrib import admin
from .models import *

class CharacterAdmin(admin.ModelAdmin):
	list_display = ['is_active', 'name', 'faction']

class PlanetAdmin(admin.ModelAdmin):
	list_display = ['is_active', 'name', 'host']

class PlanetTypeAdmin(admin.ModelAdmin):
	list_display = ['name', ]

class SpeciesAdmin(admin.ModelAdmin):
	list_display = ['name', ]

class FactionAdmin(admin.ModelAdmin):
	list_display = ['name', ]

class UnitAdmin(admin.ModelAdmin):	
	list_display = ['name', 'faction']

class ShipAdmin(admin.ModelAdmin):
	list_display = ['name', 'faction']

admin.site.register(Account)
admin.site.register(Character, CharacterAdmin)
admin.site.register(Planet, PlanetAdmin)
admin.site.register(PlanetType, PlanetTypeAdmin)
admin.site.register(Species, SpeciesAdmin)
admin.site.register(Faction, FactionAdmin)
admin.site.register(Unit, UnitAdmin)
admin.site.register(Ship, ShipAdmin)
