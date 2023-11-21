
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from .serializers import *
from core.models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()
from core.forms import *
from django.http import FileResponse
from django.conf import settings
from xhtml2pdf import pisa
from django.http import HttpResponse
import os
from django.template.loader import get_template
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
# Solicitudes no sean rechazadas por el TOKEN.

class LoginView(APIView):
    def post(self, request):
        rut = request.data.get('rut', '')
        password = request.data.get('password', '')

        user = authenticate(request, rut=rut, password=password)

        if user is not None:
            login(request, user)

            # Obtener información adicional del usuario
            user_info = {
                'rut': user.rut,
                'nombre': user.first_name,
                'apellido': user.last_name,
                'is_superuser': user.is_superuser,
                'is_staff': user.is_staff,
                'groups': list(user.groups.values_list('name', flat=True)),
                'permisos': list(user.get_all_permissions()),
                'is_active': user.is_active,
                'date_joined': user.date_joined
            }

            return Response({'message': 'Login successful', 'user_info': user_info})
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


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
def apiveravances(request):
    if request.method == 'GET':
        listado = Avances.objects.all()
        serializer = AvancesSerializer(listado, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def apitareas(request):
    if request.method == 'GET':
        listado = Tareas.objects.all()
        serializer = TareasSerializer(listado, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def apiagregaravances(request):
    if request.method == 'POST':
        serializer = AvancesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE'])   
def apieditaravances(request, pk):
    try:
        avance = Avances.objects.get(pk=pk)
    except Avances.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = AvancesSerializer(avance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        avance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)