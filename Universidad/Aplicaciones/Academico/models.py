from django.db import models

# Create your models here.


class Estudiante(models.Model):
    codigo=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    edad=models.PositiveIntegerField()

    def __str__(self) -> str:
        texto = "{0} {1} ({2})"
        return texto.format(self.nombre, self.apellido, self.edad)