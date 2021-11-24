from django.shortcuts import render
from django.http import HttpResponse
from .models import Tejidomama
# Create your views here.

def miPrimeraVista(request):
   return render(request,'miprimeraplicacion/inicio.html')

def misegundaVista(request):
     return render (request,'miprimeraplicacion/segunda.html')
  
def miterceraVista(request):
     lista = Tejidomama.objects.all()
     return render (request,'miprimeraplicacion/registro2.html',{'misdatos': lista})
  
# def micuartaVista(request):
  #  lista = Tejidomama.objects.all()
    # return render (request,'miprimeraplicacion/grafos.html', {'misdatos': [1,2,3,4]})
