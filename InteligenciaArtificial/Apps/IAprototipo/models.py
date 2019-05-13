from django.db import models

# Create your models here.

class Alumno (models.Model):
    Documento = models.CharField(max_length=20)
    Apellido1 = models.CharField(max_length=50)
    Apellido2 = models.CharField(max_length=50)
    Nombres = models.CharField(max_length=50)
    FechaNacimiento = models.DateField()
    GENERO=(('M','Masculino'), ('F', 'Femenino'))
    Sexo = models.CharField(max_length=1, choices=GENERO, default='M')


    def NombreCompleto (self):
        cadena="{0}, {1}, {2}"
        return cadena.format(self.Apellido1, self.Apellido2, self.Nombres)

