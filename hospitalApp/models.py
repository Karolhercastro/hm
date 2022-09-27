from django.db import models


class Usuario(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField('Username', max_length=20, unique=True)
    password = models.CharField('Password', max_length=20)
    create_date = models.DateField('Create date')
    activo = models.BooleanField(default=True)
    nombre = models.CharField('nombre', max_length=30)
    apellido = models.CharField('apellidos', max_length=30)
    correo = models.EmailField('correo', max_length=100)
    telefono = models.CharField('telefono', max_length=30)

    def __str__(self):
        return str(self.id)


class Auxiliar (models.Model):
    idAuxiliar = models.AutoField(primary_key=True)
    cargo = models.CharField(max_length=20)
    id_usuario = models.ForeignKey(
        Usuario, related_name='id_usuario_auxiliar',  on_delete=models.CASCADE, unique=True)

    def __str__(self):
        return str(self.idAuxiliar)


class Paciente (models.Model):
    idPaciente = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(
        Usuario, related_name='id_usuario_paciente', on_delete=models.CASCADE, unique=True)
    fecha_creacion = models.DateField('create_date')
    direccion = models.CharField('residencia', max_length=50)
    ciudad = models.CharField('ciudad', max_length=20)
    id_registro = models.ForeignKey(
        Auxiliar, related_name='id_auxiliar_registro_paciente', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.idPaciente)
