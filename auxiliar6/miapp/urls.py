from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('added_project/', views.added_project, name='added_project'),
	path('add_proyecto', views.add_proyecto, name='add_proyecto'),
	path('new_project/', views.new_project, name='new_project'),
	path('lista_proyectos/',views.lista_proyectos, name='lista_proyectos'),
	path('lista_estudiantes/', views.lista_estudiantes, name='lista_estudiantes'),
]

