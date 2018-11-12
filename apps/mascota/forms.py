from django import forms
from apps.mascota.models import Mascota

class MascotaForm(forms.ModelForm):
	class Meta:
		model = Mascota

		fields = [
		'nombre',
		'edad',
		'raza',
		'FechaRescate',
		'estado',
		'Foto',
		]

		labels = {
		'nombre': 'Nombre',
		'edad': 'Edad',
		'raza': 'Raza',
		'FechaRescate':'Fecha de Rescate',
		'estado': 'Estado',
		'Foto': 'Foto de la Mascota',
		}

		widgets = {
		'nombre': forms.TextInput(attrs={'class':'form-control'}),
		'edad': forms.TextInput(attrs={'class':'form-control'}),
		'raza': forms.TextInput(attrs={'class':'form-control'}),
		'FechaRescate': forms.DateTimeInput(attrs={'class':'form-control'}),
		'estado': forms.Select(attrs={'class':'form-control'}),
		'Foto': forms.FileInput(),
		}