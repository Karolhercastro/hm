from rest_framework import serializers
from .models import Usuario, Auxiliar, Paciente


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('__all__')
        
        
        
        
        
class AuxiliarSerializer(serializers.ModelSerializer):
    id_usuario: UsuarioSerializer()
    class Meta:
        model = Auxiliar
        fields = ('__all__')
        
        
        
        
class PacienteSerializer(serializers.ModelSerializer):
    id_usuario: UsuarioSerializer()
    id_registro: AuxiliarSerializer()
    class Meta:
        model = Paciente
        fields = ('__all__')