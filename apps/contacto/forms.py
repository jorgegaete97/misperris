from django import forms
from apps.contacto.models import Formulario


class FormularioContacto(forms.ModelForm):
	class Meta:
		model = Formulario

		fields = [
		'nombres',
		'apellidos',
		'rut',
		'telefono',
		'email',
		'fecha',
		'region',
		'ciudad',
		'vivienda',
		]

		labels = {
		'nombres': 'Nombres',
		'apellidos': 'Apellidos',
		'rut': 'Rut',
		'telefono': 'Telefono',
		'email': 'Email',
		'fecha': 'Fecha de nacimiento',
		'region': 'Region',
		'ciudad': 'Ciudad',
		'vivienda': 'Vivienda',
		}

		widgets = {
		'nombres': forms.TextInput(attrs={'class':'form-control'}),
		'apellidos': forms.TextInput(attrs={'class':'form-control'}),
		'rut': forms.TextInput(attrs={'class':'form-control'}),
		'telefono': forms.TextInput(attrs={'class':'form-control'}),
		'email': forms.EmailInput(attrs={'class':'form-control'}),
		'fecha': forms.DateTimeInput(attrs={'class':'form-control'}),
		'region': forms.Select(attrs={'class':'form-control'}),
		'ciudad': forms.TextInput(attrs={'class':'form-control'}),
		'vivienda': forms.Select(attrs={'class':'form-control'}),
		}