from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "base/index.html")

def manual_de_usuario(request):
    return render(request, 'home/manual_de_usuario.html')

def descripcion(request):
    return render(request, 'gmys/proyecto.html', {'titulo': 'La Importancia de Planificar Antes de Codificar'})

def miDoctorYa(request):
    return render(request, 'midoctorya/proyecto.html', {'titulo': 'Preámbulo del Proyecto de Gestión de Pacientes'})    
