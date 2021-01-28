from django.shortcuts import render, redirect
from .models import User
# Create your views here.

def home(request):
    return render(request, "home.html")

def setCI(request):
    return render(request, "prueba.html")

def checkIfUserExists(request):
    identifier = request.POST['identifier']
    try:
        user = User.objects.get(identifier=identifier)
    except User.DoesNotExist:
        user = User(identifier=identifier, name='Stephaniec',lastname='Cruz',birthday='2020-02-02')
        user.save()
        return redirect('/xx')
    return render(request,'user_data.html')