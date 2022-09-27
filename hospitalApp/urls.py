from django.urls import path
from .views import UsuarioList, UsuarioDetail, AuxiliarList, AuxiliarDetail, PacienteList, PacienteDetail
from hospitalApp import views


urlpatterns = [
    path('usuario/', UsuarioList.as_view()),
    path('usuario/<int:pk>/', UsuarioDetail.as_view()),
    path('auxiliar/', AuxiliarList.as_view()),
    path('auxiliar/<int:pk>/', AuxiliarDetail.as_view()),
    path('paciente/', PacienteList .as_view()),
    path('paciente/<int:pk>/', PacienteDetail.as_view()),
    path('busqueda_usuario/', views.busqueda_usuarios),
    path('buscar/', views.buscar),
]
