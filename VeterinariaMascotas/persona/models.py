from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from datetime import datetime

class Registro(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField(auto_now_add=True)


# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


#Modelo tipo de animal
class TipoAnimal(models.Model):
    nombreTipo = models.CharField(max_length=50)

    def __str__(self):
        return self.nombreTipo

#Modelo de animal
class Animal(models.Model):
    idTipoAnimal = models.ForeignKey(TipoAnimal, on_delete = models.CASCADE)
    idDueno = models.ForeignKey(Persona, on_delete = models.CASCADE, null = True)
    nombreAnimal = models.CharField(max_length=50)
    fechaNacimiento = models.DateField('Fecha de Nacimiento')
    raza = models.CharField(max_length=50)
    sexo = models.CharField(max_length=50)
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    observaciones = models.TextField()
    imagen = models.ImageField(upload_to='animal_images/', null=True, blank=True)

    def calcular_edad(self):
        today = datetime.today()
        age = today.year - self.fechaNacimiento.year - ((today.month, today.day) < (self.fechaNacimiento.month, self.fechaNacimiento.day))
        return age

    def __str__(self):
        return self.nombreAnimal
    
class Medicina(models.Model):
    nombreMedicamento = models.CharField(max_length=50)

    def __str__(self):
        return self.nombreMedicamento


class Consulta(models.Model):
    idAnimal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    sintomas = models.TextField()
    observaciones = models.TextField()
    diagnostico = models.TextField()
    fechaConsulta = models.DateField('Fecha Consulta:', null=True)
    receta = models.ManyToManyField(Medicina, through='Medicacion')


class Medicacion(models.Model):
    medicina = models.ForeignKey(Medicina, on_delete=models.CASCADE)
    consulta = models.ForeignKey(Consulta, on_delete=models.CASCADE)

class MedicacionInLine(admin.TabularInline):
    model = Medicacion
    extra = 1

class ConsultaAdmin(admin.ModelAdmin):
    inlines = (MedicacionInLine,)

class MedicinaAdmin(admin.ModelAdmin):
    inlines = (MedicacionInLine,)


    


