from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(User)
admin.site.site_header = 'Administración de Craftify'
admin.site.index_title = 'Craftify'
admin.site.site_title = 'Administración de Craftify'

admin.site.register(Proyecto)
admin.site.register(CategoriaProyecto)
admin.site.register(StatusProyecto)
admin.site.register(Clientes)