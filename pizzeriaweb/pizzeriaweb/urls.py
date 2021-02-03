from rest_framework import routers
from django.urls import path
from django.contrib import admin
from modules.pizzas.viewsets import PizzaViewSet, UserViewSet, SizeViewSet, IngredientViewSet, SalesViewSet, DrinkViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pizza-list', PizzaViewSet.pizzaList, name = "pizza-list"),
    path('create-pizza', PizzaViewSet.createPizza, name = "create-pizza"),
    path('get-user/<int:entryId>', UserViewSet.getUser, name = "get-user"),
    path('create-user', UserViewSet.createUser, name = "create-user"),
    path('get-sizes', SizeViewSet.getSizes, name = "get-sizes"),
    path('get-drinks', DrinkViewSet.getDrinks, name = "get-drinks"),
    path('get-ingredients', IngredientViewSet.getIngredients, name = "get-ingredients"),
    path('last-order', PizzaViewSet.lastOrderId, name = "last-order"),
    path('salesBySize/<int:entryId>', SalesViewSet.salesBySize, name = "salesBySize"),
    path('salesByIngredient/<int:entryId>', SalesViewSet.salesByIngredient, name = "salesByIngredient"),
    path('salesByUser/<int:entryId>', SalesViewSet.salesByUser, name = "salesByUser"),
    path('sales', SalesViewSet.sales, name = "sales")
]