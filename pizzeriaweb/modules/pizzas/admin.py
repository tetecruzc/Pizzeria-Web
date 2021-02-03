from django.contrib import admin
from django.db.models.functions import Lower
from .models import User, Pizza, Ingredient, Size, Drink
# Register your models here.

def custom_titled_filter(title):
    class Wrapper(admin.FieldListFilter):
        def __new__(cls, *args, **kwargs):
            instance = admin.FieldListFilter.create(*args, **kwargs)
            instance.title = title
            return instance
    return Wrapper

class PizzaAdmin(admin.ModelAdmin):
    list_display = ["orderId", "date", "nameUser", "totalPizzas", "totalDrinks", "totalPriceOrder"]
    list_filter  = (
        ( 'date' , custom_titled_filter ( 'Date' )),
        ( 'size_id' , custom_titled_filter ( 'Size pizza' )),
        ( 'user_id' , custom_titled_filter ( 'Client' )),
        ('ingedients', custom_titled_filter ( 'Ingredients' ))
    )

    def queryset(self, request, queryset):
        if 1 == 1:
            return queryset.filter(orderId = 1)

    def get_ordering(self, request):
        return [Lower('orderId')]
    
    

    def nameUser(self,obj):
        user = User.objects.get(id = obj.user_id)
        return user.name
    
    def totalPizzas(self,obj):
        pizzasByOrder = Pizza.objects.filter(orderId = obj.orderId)
        count = 0
        for pizza in pizzasByOrder:
            count = count + 1
        return count

    def totalDrinks(self,obj):
        pizzasByOrder = Pizza.objects.filter(orderId = obj.orderId)
        count = 0
        for pizza in pizzasByOrder:
            if (pizza.drink):
                count = count + 1
        return count
    
    def totalPriceOrder(self,obj):
        pizzasByOrder = Pizza.objects.filter(orderId = obj.orderId)
        totalPriceOrder = 0
        for pizza in pizzasByOrder:
            totalPriceOrder = totalPriceOrder + pizza.totalPrice
        return totalPriceOrder
    
    

admin.site.register(Pizza, PizzaAdmin)
admin.site.register(User)
admin.site.register(Ingredient)
admin.site.register(Size)
admin.site.register(Drink)
