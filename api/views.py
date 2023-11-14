from typing import Any
from django import http
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
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
from django.http import FileResponse
from django.conf import settings
from xhtml2pdf import pisa
from django.http import HttpResponse
import os
from django.template.loader import get_template
from django.utils.decorators import method_decorator
# Create your views here.
# Solicitudes no sean rechazadas por el TOKEN.

@csrf_exempt
@api_view(['GET'])
def cotizaciones_pdf_api(request, id_cotizacion):
    cotizacion = get_object_or_404(Cotizaciones, id_cotizacion=id_cotizacion)

    template = get_template('cotizaciones/cotizacionpdf.html')
    context = {
        'cotizaciones': cotizacion,
        'comp': {'nombre': 'Gabinet Center', 'rut': '123456789', 'direccion': 'Virgen del Pilar 0389', 'ciudad': 'Santiago'},
    }
    html = template.render(context)

    nombre_archivo_cliente = f'Cotizacion {cotizacion.cliente.nombre} {cotizacion.cliente.apellido}-{cotizacion.nombre_cotizacion}-{cotizacion.fecha_cotizacion}.pdf'

    destino_pdf = os.path.join(settings.MEDIA_ROOT, 'pdfcot', nombre_archivo_cliente)

    pisa_status = pisa.CreatePDF(html, open(destino_pdf, "wb"))

    if pisa_status.err:
        return HttpResponse("Error al generar el PDF", content_type='text/plain')

    response = FileResponse(open(destino_pdf, 'rb'))
    response['Content-Disposition'] = f'attachment; filename="{nombre_archivo_cliente}"'

    return response


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
def apistatus(request):
    if request.method == 'GET':
        listado = StatusProyecto.objects.all()
        serializer = StatusSerializer(listado, many=True)
        return Response(serializer.data)
    


@api_view(['GET'])
def apiproductos(request):
    if request.method == 'GET':
        listado = Productos.objects.all()
        serializer = ProductosSerializer(listado, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def apiclientes(request):
    if request.method == 'GET':
        listado = Clientes.objects.all()
        serializer = ClienteSerializer(listado, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

