from rest_framework import viewsets
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.serializers import Serializer
from .models import Ingredient, Pizza, Size, User, Drink
from .serializer import PizzaSerializer, UserSerializer, SizeSerializer, IngredientSerializer, DrinkSerializer

class PizzaViewSet(viewsets.ModelViewSet):
    @api_view(['GET'])
    def pizzaList(request):
        try:
            pizzas = Pizza.objects.all()
            serializer = PizzaSerializer(pizzas, many=True)
            return Response(serializer.data)
        except Pizza.DoesNotExist as Ex:
            return Response( {'Error': '401', 
            'Description': 'No pizza found'})
    
    @api_view(['POST'])
    def createPizza(request):
        is_many = isinstance(request.data,list)
        serializer = PizzaSerializer(data = request.data, many = is_many)
        if (serializer.is_valid() is False):
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(serializer.data)

    @api_view(['GET'])
    def lastOrderId(request):
        try:
            order = Pizza.objects.order_by('-orderId')[0]
            serializer = PizzaSerializer(order, many=False)
            return Response(serializer.data)
        except Pizza.DoesNotExist as Ex:
            return Response( {'Error': '401', 
            'Description': 'No order found'})
    


class UserViewSet(viewsets.ModelViewSet):
    @api_view(['GET'])
    def getUser(request,entryId):
        try:
            user = User.objects.get(id = entryId)
            serializer = UserSerializer(user,many=False)
            return Response(serializer.data)
        except User.DoesNotExist as Ex:
            return Response( {'Error': '401', 
            'Description': 'User not found'})


    @api_view(['POST'])
    def createUser(request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)


class SizeViewSet(viewsets.ModelViewSet):
    @api_view(['GET'])
    def getSizes(request):
        try:
            sizes = Size.objects.all()
            serializer = SizeSerializer(sizes, many=True)
            return Response(serializer.data)
        except Size.DoesNotExist as Ex:
            return Response( {'Error': '401', 
            'Description': 'No size found'})

class DrinkViewSet(viewsets.ModelViewSet):
    @api_view(['GET'])
    def getDrinks(request):
        try:
            drinks = Drink.objects.all()
            serializer = DrinkSerializer(drinks, many=True)
            return Response(serializer.data)
        except Drink.DoesNotExist as Ex:
            return Response( {'Error': '401', 
            'Description': 'No Drink found'})

class IngredientViewSet(viewsets.ModelViewSet):
    @api_view(['GET'])
    def getIngredients(request):
        try:
            ingredients = Ingredient.objects.all()
            serializer = IngredientSerializer(ingredients, many=True)
            return Response(serializer.data)
        except Ingredient.DoesNotExist as Ex:
            return Response( {'Error': '401', 
            'Description': 'No ingredient found'})

class SalesViewSet(viewsets.ModelViewSet):
    @api_view(['GET'])
    def salesBySize(request, entryId):
        try:
            sales = Pizza.objects.filter(size = entryId)
            serializer = PizzaSerializer(sales, many = True)
            return Response(serializer.data)
        except Pizza.DoesNotExist as Ex:
            return Response( {'Error': '401', 
            'Description': 'No Size found'})

    @api_view(['GET'])
    def salesByIngredient(request, entryId):
        try:
            sales = Pizza.objects.filter(ingedients = entryId)
            serializer = PizzaSerializer(sales, many = True)
            return Response(serializer.data)
        except Pizza.DoesNotExist as Ex:
            return Response( {'Error': '401', 
            'Description': 'No Ingredient found'})
    

    @api_view(['GET'])
    def salesByUser(request, entryId):
        try:
            sales = Pizza.objects.filter(user = entryId).order_by('date')
            serializer = PizzaSerializer(sales, many = True)
            return Response(serializer.data)
        except Pizza.DoesNotExist as Ex:
            return Response( {'Error': '401', 
            'Description': 'No User found'})


    @api_view(['GET'])
    def sales(request):
        try:
            sales = Pizza.objects.all().order_by('orderId')
            serializer = PizzaSerializer(sales, many = True)
            return Response(serializer.data)
        except Pizza.DoesNotExist as Ex:
            return Response( {'Error': '401', 
            'Description': 'No User found'})
    


    


    


