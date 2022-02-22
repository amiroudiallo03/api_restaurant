from rest_framework import serializers
from . import models


class PersonneSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Personne
        fields = ['last_name', 'first_name', 'number']
        

class MenuSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Menu
        fields = ['name', 'price', 'image']
        

class CommandeSerializers(serializers.ModelSerializer):
    
   
    class Meta:
        model = models.Commande
        exclude = ['date_add', 'date_update', 'status']
        depth = 1
        


