from django.conf.urls import url, include
from apps.contacto.views import index,formulario_view, Contacto_List


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^nuevo$', formulario_view, name='formulario_crear'),
    url(r'^ver$', Contacto_List, name='Contacto_Listar'),
]