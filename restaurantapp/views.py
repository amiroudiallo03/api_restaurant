import numbers
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models
from .serializers import PersonneSerializers, MenuSerializers, CommandeSerializers
import re
# Create your views here.
def check_number(numero: str):
    reg = re.compile('(00255|\d{2})(?P<debut> ([-_ ]?\d{2}){3})')
    operateur = reg.match(numero)
    if operateur:
        return True
    return False

def client_exists(number: str):
    try:
        academician = models.Personne.objects.get(number=number)
        return True
    except models.Personne.DoesNotExist:
        return False


@api_view(["GET","POST"])
def api_client(request):
    if request.method == 'GET':
        clients = models.Personne.objects.all()
        serializer = PersonneSerializers(clients, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        numero = request.data.get('number')
        if client_exists(numero):
            return Response({"message":'Client déjà enregistré !!!'})
        elif not check_number(numero):
            return Response({'message':'Numéro invalide'})
        else:
            serializer = PersonneSerializers(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Client bien enregistré'})


@api_view(['GET','POST'])
def api_menu(request):
    if request.method == 'GET':
        menus = models.Menu.objects.all()
        serializer = MenuSerializers(menus, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MenuSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Menu ajouté'})


@api_view(['GET','POST'])
def api_commande(request):
    if request.method == 'GET':
        commandes = models.Commande.objects.all()
        serializer = CommandeSerializers(commandes, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        numbers = request.data.get('number')
        client = models.Personne.objects.get(number=numbers)
        menu = request.data.get('name')
        menus = models.Menu.objects.get(name=menu)
        if not menus:
            return Response({'message':'Répas choisis non disponible '})
        if client_exists(numbers):
            commandes = models.Commande.objects.create(personne=client,menu=menus)
            commandes.save()

            return Response({'message': 'Commande bien enregistré'})
        else:
            return Response({'message':"Veillez enregistré le client d'abord"})

        


