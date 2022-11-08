from django.shortcuts import render, redirect
from .models import Estudiante
from django.contrib import messages

# Create your views here.


def home(request):
    estudiantesListados = Estudiante.objects.all()
    messages.success(request, '¡Estudiantes listados!')
    return render(request, "gestionEstudiantes.html", {"estudiantes": estudiantesListados})

def registrarEstudiante(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    apellido=request.POST['txtApellido']
    edad=request.POST['numEdad']

    estudiante=Estudiante.objects.create(codigo=codigo, nombre=nombre, apellido=apellido, edad=edad)
    messages.success(request, '¡Estudiante registrado!')
    return redirect('/')

def editarEstudiante(request, codigo):
    estudiante = Estudiante.objects.get(codigo=codigo)
    return render(request, "edicionEstudiante.html", {'estudiante':estudiante})

def edicionEstudiante(request):
    codigo=request.POST['txtCodigo']
    nombre=request.POST['txtNombre']
    apellido=request.POST['txtApellido']
    edad=request.POST['numEdad']

    estudiante = Estudiante.objects.get(codigo=codigo)
    estudiante.nombre = nombre
    estudiante.apellido = apellido
    estudiante.edad = edad
    estudiante.save()

    messages.success(request, '¡Estudiante actualizado!')

    return redirect('/')

def eliminarEstudiante(request, codigo):
    estudiante = Estudiante.objects.get(codigo=codigo)
    estudiante.delete()

    messages.success(request, '¡Estudiante eliminado!')

    return redirect('/')