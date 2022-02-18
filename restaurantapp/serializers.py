from dataclasses import field
from rest_framework import serializers
from . import models


class PersonneSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Personne
        exclude = ['date_add', 'date_update', 'status']

class MenuSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Menu
        exclude = ['date_add', 'date_update', 'status']

class CommandeSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Commande
        exclude = ['date_add', 'date_update', 'status']

