from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "base/index.html")

def manual_de_usuario(request):
    return render(request, 'home/manual_de_usuario.html')