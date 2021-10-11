from django.urls import include, path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'item', ItemViewSet, basename="item")
router.register(r'user', UserViewSet, basename="user")
router.register(r'sales', SalesViewSet, basename="sales")
router.register(r'item/<str:pk>/', ItemViewSet, basename="item")
router.register(r'item/<str:pk>/<int:quantity>/', ItemViewSet, basename="item")
router.register(r'user<str:pk>/', UserViewSet, basename="user")
router.register(r'sales/<int:pk>/', SalesViewSet, basename="sales")
router.register(r'monthly-purchase', MonthlyPurchaseViewSet, basename="monthly")
router.register(r'monthly-purchase/<str:pk>/', MonthlyPurchaseViewSet, basename="monthly")

urlpatterns = [
    path('api/', include(router.urls)),
]