from django.db import models

# Create your models here.
class Ingredient(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        txt = "Ingrediente {0}"
        return txt.format(self.name)


class Size(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    
    def __str__(self):
        txt = "Tamaño {0}"
        return txt.format(self.name)

class User(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    birthday = models.DateField()

    def __str__(self):
        txt = "User {0} {1}"
        return txt.format(self.name, self.lastname)

class Pizza(models.Model):
    ingedients = models.ManyToManyField(Ingredient)
    #ingredients = models.ForeignKey(Ingredient,null=True,on_delete=models.CASCADE)# models.ForeignKey(Ingredient, null=True,blank=False,on_delete=models.CASCADE)
    size = models.ForeignKey(Size, null=False,blank=False,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, null=False,blank=False,on_delete=models.CASCADE)
    orderId = models.PositiveIntegerField()

    def __str__(self):
        txt = "Pizza {0}"
        return txt.format(self.id)



'''
class Order(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    pizza = models.ForeignKey(Pizza, null=False,blank=False,on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=False,blank=False,on_delete=models.CASCADE)
    
    def __str__(self):
            txt = "Order number {0}"
            return txt.format(self.id)
'''
