from django.conf.urls import url, include
from apps.Index.views import index, RegistroUsuario, cliente, Mascota_List,Mascota_Edit

from django.urls import include, path

app_name = "index";

urlpatterns = [
url(r'^$', index,name='Menu'),
url(r'^registrar$', RegistroUsuario.as_view()),
url(r'^cliente', cliente, name='Cliente' ),
url(r'^adoptar$', Mascota_List, name='Mascota_Listar'),
path('adopcion/<str:nombre>/' ,Mascota_Edit, name='mascota_editar'),
]