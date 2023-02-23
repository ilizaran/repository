from django.conf.urls import  include, url

from record import views

urlpatterns = [
    url(r'^(?P<idt>\d+)$', views.mostrar_registro, name='mostrar_registro'),
    url(r'^coleccion/(?P<col>\d+)$', views.listado_por_coleccion, name='listado_por_coleccion'),
    url(r'^material/(?P<mat>\d+)$', views.listado_por_tipo_material, name='listado_por_tipo_material'),
    url(r'^lugares/(?P<lu>\d+)$', views.listado_por_lugares, name='listado_por_lugares'),
    ]
