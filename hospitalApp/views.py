from rest_framework import generics


from .models import Usuario, Auxiliar, Paciente
from .serializers import UsuarioSerializer, AuxiliarSerializer, PacienteSerializer

# imports para el html
from django.shortcuts import render
from django.http import HttpResponse


class AuxiliarList(generics.ListCreateAPIView):
    serializer_class = AuxiliarSerializer

    def get_queryset(self):
        queryset = Auxiliar.objects.all()
        location = self.request.query_params.get('location')
        if location is not None:
            queryset = queryset.filter(id_usuario=location)
        return queryset


class AuxiliarDetail (generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AuxiliarSerializer
    queryset = Auxiliar.objects.all()


class UsuarioList(generics.ListCreateAPIView):
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()


class UsuarioDetail (generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()


class PacienteList(generics.ListCreateAPIView):
    serializer_class = PacienteSerializer

    def get_queryset(self):
        queryset = Paciente.objects.all()
        location = self.request.query_params.get('location')
        if location is not None:
            queryset = queryset.filter(id_usuario=location)
        return queryset


class PacienteDetail (generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PacienteSerializer
    queryset = Paciente.objects.all()

    # definimos las funciones para el front


def busqueda_usuarios(request):
    return render(request, "busqueda_usuarios.html")


def buscar(request):
    return render(request="buscar")
  
