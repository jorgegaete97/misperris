from django.db import models

# Create your models here.

class Mascota(models.Model):
	nombre = models.CharField(max_length = 50)
	edad = models.IntegerField()
	raza = models.CharField(max_length=50)
	FechaRescate = models.DateField()

	estados=(('Disponible','Se encuentra Disponible'),('No disponible','No se encuentra Disponible'))
	estado=models.CharField(max_length=50,choices=estados,default='Disponible')

	Foto = models.ImageField(upload_to="projects")
