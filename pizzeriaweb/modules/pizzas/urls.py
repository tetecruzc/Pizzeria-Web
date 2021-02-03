from rest_framework import routers
from django.urls import path
from .viewsets import PizzaViewSet, UserViewSet

urlpatterns = [
    path('', PizzaViewSet.apiOverView, name = "api-overview"),
    path('pizza-list', PizzaViewSet.pizzaList, name = "pizza-list"),
    path('get-user/<int:entryId>', UserViewSet.getUser, name = "get-user")
]
