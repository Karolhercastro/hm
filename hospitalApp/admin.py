from django.contrib import admin

from .models import Usuario, Auxiliar, Paciente

admin.site.register(Usuario)
admin.site.register(Auxiliar)
admin.site.register(Paciente)
