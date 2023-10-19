from django.test import TestCase
from .models import User, Clientes, Proyecto, CategoriaProyecto, StatusProyecto

class UserTestCase(TestCase):
    def test_user_creation(self):
        user = User.objects.create_user('123', '123')
        self.assertEqual(user.rut, '123')

class ClientesTestCase(TestCase):
    def test_client_creation(self):
        cliente = Clientes(rut_cliente=123, nombre="Juan", apellido="Pérez", direccion="Calle X", telefono="123456789")
        cliente.save()
        self.assertEqual(cliente.nombre, "Juan")

class ProyectoTestCase(TestCase):
    def test_proyecto_creation(self):
        cliente = Clientes(rut_cliente=123, nombre="Juan", apellido="Pérez", direccion="Calle X", telefono="123456789")
        cliente.save()
        
        # Crea instancias de CategoriaProyecto y StatusProyecto
        categoria = CategoriaProyecto.objects.create(id_categoria=1, nombre_categoria="Categoria de Prueba")
        status = StatusProyecto.objects.create(id_status=1, nombre_status="Status de Prueba")
        
        proyecto = Proyecto(id_proyecto=1, cliente=cliente, categoria=categoria, status=status, nombre_proyecto="Proyecto1", instalacion=False, fecha="2023-10-19", plazo_entrega="2023-10-30")
        proyecto.save()
        
        self.assertEqual(proyecto.nombre_proyecto, "Proyecto1")
