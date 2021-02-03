from rest_framework import routers
from .viewsets import PizzaViewSet, SalesBySizeViewSet

router = routers.SimpleRouter()
router.register('pizzas', PizzaViewSet)

urlpatterns = router.urls
