from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from apps.mascota.models import Mascota

from apps.mascota.forms import MascotaForm

from django.urls import reverse_lazy

from apps.Index.forms import RegistroForm


from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.






def index(request):
	return render(request, 'MisPerris/index.html')


def cliente(request):
	return render(request, 'MisPerris/menu_cliente.html')



class RegistroUsuario(CreateView):
	model = User
	template_name = "MisPerris/registrarse.html"
	form_class = RegistroForm
	success_url = reverse_lazy('login')



def Mascota_List(request):
	mascota = Mascota.objects.all()
	contexto = {'mascotas':mascota}
	return render(request,'MisPerris/adoptar.html',contexto)



def Mascota_Edit(request, nombre):
	mascota = Mascota.objects.get(nombre = nombre)
	if request.method == 'GET':
		form = MascotaForm(instance=mascota)
	else:
		form = MascotaForm(request.POST, request.FILES or None, instance=mascota)
		if form.is_valid():
			form.save()
		return redirect('index:Cliente')
	return render(request, 'MisPerris/EditarMascota.html',{'form': form})