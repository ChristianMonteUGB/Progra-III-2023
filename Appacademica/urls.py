from django.contrib import admin
from django.urls import path
from appalumnos.views import saludo, miEdad, index, alumnos, busqueda_alumnos, materias, busqueda_materias

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('edad/<int:edad>/', miEdad),
     path('', index),
    path('frmalumnos', alumnos),
    path('frmmaterias', materias),
    path('frmbusqueda_alumnos', busqueda_alumnos),
    path('frmbusqueda_materias', busqueda_materias),
]