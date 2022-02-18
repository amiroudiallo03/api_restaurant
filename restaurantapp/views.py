from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models
from .serializers import PersonneSerializers
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

