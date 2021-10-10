from django.urls import include, path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'item', ItemViewSet)
router.register(r'user', UserViewSet)
router.register(r'sales', SalesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]