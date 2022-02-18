from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Personne)
class PersonnesAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'number']

@admin.register(models.Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']

@admin.register(models.Commande)
class CommandeAdmin(admin.ModelAdmin):
    list_display = ['personne', 'menu']
    