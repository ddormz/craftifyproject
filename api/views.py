from django.shortcuts import render
from .serializers import *
from core.models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token
from rest_framework.decorators import permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

@csrf_exempt # Solicitudes no sean rechazadas por el TOKEN.

@api_view(['GET', 'POST',] ) #put, delete.

def listarProyectos(request):
    if request.method == 'GET':
        listado = Proyecto.objects.all()
        serializer = ProyectosSerializer(listado, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProyectosSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)