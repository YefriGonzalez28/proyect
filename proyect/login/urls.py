from django.contrib import admin
from django.urls import path
from django import views
from  login import views


urlpatterns = [
    path('',views.index, name="index"),
    path('dashboard.html',views.dashboard, name="dashboard"),
    path('buscar.html',views.buscar, name="buscar un contrato"),
    path('registra.html',views.editar, name="registrar nuevo contrato"),
    path('editar_contrato.html',views.editar, name="editar un contrato"),
    path('eliminar_contrato.html',views.editar, name="eliminar un contrato"),
    path('cargar_contrato.html',views.editar, name="cargar un contrato"),
    path('actualizar_contrato.html',views.editar, name="actualizar un contrato"),
]
