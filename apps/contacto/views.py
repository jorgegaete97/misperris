from django.shortcuts import render, redirect
from django.http import HttpResponse

from apps.contacto.forms import FormularioContacto
from apps.contacto.models import Formulario

# Create your views here.

def index(request):
	return render(request, 'MisPerris/index.html')



def formulario_view(request):
	if request.method == 'POST':
		form = FormularioContacto(request.POST)
		if form.is_valid():
			form.save()
		return redirect('index:Menu')
	else:
		form = FormularioContacto()

	return render(request, 'MisPerris/contactar_form.html',{'form':form})


def Contacto_List(request):
	contacto = Formulario.objects.all()
	contexto = {'contactos':contacto}
	return render(request,'MisPerris/listar_cliente.html',contexto)