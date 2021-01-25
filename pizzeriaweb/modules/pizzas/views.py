from django.shortcuts import render
from .models import User
# Create your views here.


def pruebaPrimerTemplate(request):
    return render(request, "prueba.html")

def pruebaRedireccion(request):
    identifier = request.POST['identifier']
    try:
        user = User.objects.get(identifier=identifier)
    except User.DoesNotExist:
        user = User(identifier=identifier, name='Stephaniec',lastname='Cruz',birthday='2020-02-02')
        user.save()
    return render(request,'prueba.html')