from django.conf.urls import url, include
from apps.mascota.views import index, Mascota_view, Mascota_List



app_name = "mascota";

urlpatterns = [
url(r'^$', index, name='index'),
url(r'^nuevo$', Mascota_view, name='Mascota_Crear'),
url(r'^ver$', Mascota_List, name='Mascota_Listar'),


]