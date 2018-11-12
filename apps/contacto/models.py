from django.db import models

class Formulario(models.Model):
	nombres = models.CharField(max_length = 50)
	apellidos = models.CharField(max_length=50)
	rut = models.CharField(max_length=9)
	telefono = models.CharField(max_length=8)
	email = models.EmailField()
	fecha = models.DateField()


	regiones=(('Tarapacá','Región de Tarapacá'),('Antofagasta','Región de Antofagasta'),('Atacama','Región de Atacama'),('Coquimbo','Región de Coquimbo'),
              ('Valparaiso','Región de Valparaíso'),('Bernardo Ohiggins','Región del Libertador General Bernardo OHiggins'),('Maule','Región del Maule'),
              ('Nuble','Región de Ñuble'),('BioBio','Región del Biobío'),('Araucanía','Región de la Araucanía'),('Los Rios','Región de Los Ríos'),
              ('Los Lagos','Región de Los Lagos'),('Aysen','Región de Aysén del General Carlos Ibáñez del Campo'),('Magallanes','Región de Magallanes y de la Antártica Chilena'),
              ('Santiago','Región Metropolitana de Santiago'))


	region=models.CharField(max_length=50,choices=regiones,default='Santiago')

	ciudad = models.TextField(max_length=50)


	tipodevivienda=(('Patio Grande','casa con patio grande'),('Patio Chico','casa con patio pequeño'),('Sin Patio','casa sin patio'),('Departamento','departamento'))
	vivienda = models.CharField(max_length=50,choices=tipodevivienda,default='Patio Grande')



# Create your models here.
