from django.shortcuts import render, redirect
from .models import User, Size, Ingredient, Pizza
from .forms import PizzaForm

def home(request):
    context={
             "title" : "Despues vemos qué ponemos aqui, jeje",
             "subtitle" : "Cambiaré todos los estilos al finalizar la funcionalidad"
            }
    return render(request, "home.html", context)

def order(request):
    return render(request, "order.html")


def saveUser(request,id):
    if request.method == 'POST':
        name = request.POST['name']
        lastName = request.POST['lastName']
        birthDay = request.POST['birthDay']
        ## si -> campos vacios ...
        user = User(id=id, name=name,lastname=lastName,birthday=birthDay)
        user.save()
        return redirect('step3',id=id)
    return render(request,'user_data.html')
    

def orderPizza(request,id):
    currentOrder = Pizza.objects.order_by('orderId').last()
    print(currentOrder)
    if request.method == 'POST' and 'another-pizza-btn' in request.POST:
        form = PizzaForm(request.POST)
        ##
        if form.is_valid():
            pizza = form.save(commit=False)
            pizza.user = User.objects.get(pk=id)
            pizza.orderId = currentOrder.orderId
            pizza.save()
        return redirect('step3', id=id)
    else:
        form = PizzaForm()
    return render(request,'order_pizzas.html',{'form': form})

