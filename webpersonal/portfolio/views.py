from django.shortcuts import render
from .models import Project  #para recuperar lo que guardamos

# Create your views here.

def portfolio(request):
    projects=Project.objects.all() #para recuperar todos los projectos le pasamos el diccionario
    return render(request,"portfolio/portfolio.html",{'projects':projects})