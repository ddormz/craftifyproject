from rest_framework import serializers
from core.models import *


class ProyectosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyecto
        fields = '__all__'