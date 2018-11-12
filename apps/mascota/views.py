from django.shortcuts import render, redirect
from django.http import HttpResponse

from apps.mascota.forms import MascotaForm
from apps.mascota.models import Mascota

# Create your views here.

def index(request):
	return render(request, 'MisPerris/registrar_mascota.html')


def Mascota_view(request):
	if request.method == 'POST':
		form = MascotaForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
		return redirect('index:Menu')
	else:
		form = MascotaForm()

	return render(request,'MisPerris/registrar_mascota.html',{'form':form})



def Mascota_List(request):
	mascota = Mascota.objects.all()
	contexto = {'mascotas':mascota}
	return render(request,'MisPerris/listar_mascota.html',contexto)


