from django.http import JsonResponse
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
from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework import viewsets
from core.forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.

@csrf_exempt # Solicitudes no sean rechazadas por el TOKEN.

@api_view(['GET', 'POST',] ) #put, delete.
def apidetallecotizaciones(request):
    if request.method == 'GET':
        listado = DetalleCotizaciones.objects.all()
        serializer = DetalleCotizacionSerializer(listado, many=True)
        return Response(serializer.data)

@api_view(['GET', 'POST',] ) #put, delete.

def apicotizaciones(request):
    listado = Cotizaciones.objects.all()
    serializer = CotizacionesSerializer(listado, many=True)
    return Response(serializer.data)

@api_view(['GET', 'POST'])

def apiproyectos(request):
    listado = Proyecto.objects.all()
    serializer = ProyectosSerializer(listado, many=True)
    return Response(serializer.data)


@api_view(['GET'])    
def apitrabajadores(request):
    if request.method == 'GET':
        listado = User.objects.all()
        serializer = TrabajadoresSerializer(listado, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def apiproductos(request):
    if request.method == 'GET':
        listado = Productos.objects.all()
        serializer = ProductosSerializer(listado, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def apicategorias(request):
    if request.method == 'GET':
        listado = CategoriaProductos.objects.all()
        serializer = CategoriaProductosSerializer(listado, many=True)
        return Response(serializer.data)


@api_view(['GET'])  
def apisubcategorias(request):
    if request.method == 'GET':
        listado = SubcategoriaProductos.objects.all()
        serializer = SubcategoriaProductosSerializer(listado, many=True)
        return Response(serializer.data)

@api_view(['GET'])    
def apimarcas(request):
    if request.method == 'GET':
        listado = MarcaProductos.objects.all()
        serializer = MarcaProductosSerializer(listado, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def apivariantes(request):
    if request.method == 'GET':
        listado = VarianteProductos.objects.all()
        serializer = VariantesSerializer(listado, many=True)
        return Response(serializer.data)
@api_view(['GET'])  
def apiveravances(request):
    if request.method == 'GET':
        listado = Avances.objects.all()
        serializer = AvancesSerializer(listado, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def apiequipos(request):
    if request.method == 'GET':
        listado = Equipos.objects.all()
        serializer = EquiposSerializer(listado, many=True)
        return Response(serializer.data)


@api_view(['GET'])   
def apiasignaciones(request):
    if request.method == 'GET':
        listado = EquipoAsignacion.objects.all()
        serializer = AsignacionesSerializer(listado, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def apistatus(request):
    if request.method == 'GET':
        listado = StatusProyecto.objects.all()
        serializer = StatusSerializer(listado, many=True)
        return Response(serializer.data)
    

