from django.shortcuts import render
from .models import Estudiante, Proyecto, Grupo, Desafio, DesafiosEstudiantes
#from .models import Proyecto


# Create your views here.
def index(request):
	return render(request, 'miapp/index.html')

def added_project(request):
	return render(request, 'miapp/added_project.html')

def add_proyecto(request):
	descripcion = request.POST['descripcion']
	cliente =request.POST['cliente']
	fecha = request.POST['fecha_limite']

	contexto = {"form":"Formulario creado con exito", "gracias":"Muchas gracias",
	 "descripcion":descripcion, "cliente":cliente, "fecha":fecha}
	
	proyecto = Proyecto(descripcion=descripcion, cliente=cliente, fecha_limite=fecha)
	proyecto.save()
	
	return render(request, 'miapp/added_project.html', contexto)

def new_project(request):
	return render(request, 'miapp/new_project.html')

def lista_estudiantes(request):
	contexto={}
	contexto['estudiantes'] = Estudiante.objects.all()
	return render(request, 'miapp/lista_estudiantes.html',contexto)

def lista_proyectos(request):
	contexto={}
	contexto['proyectos'] = Proyecto.objects.all()
	return render(request, 'miapp/lista_proyectos.html', contexto)


