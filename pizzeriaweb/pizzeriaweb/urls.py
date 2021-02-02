"""pizzeriaweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from modules.pizzas.views import order
from modules.pizzas.views import home
#from modules.pizzas.views import checkIfUserExists
from modules.pizzas.views import saveUser
from modules.pizzas.views import userInfo
from modules.pizzas.views import orderPizza

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1.0/', include("modules.pizzas.urls")) 
]   