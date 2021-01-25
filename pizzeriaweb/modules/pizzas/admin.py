from django.contrib import admin
from modules.pizzas.models import *
# Register your models here.


admin.site.register(Pizza)
admin.site.register(Ingredient)
admin.site.register(Size)
admin.site.register(User)
admin.site.register(Order) 