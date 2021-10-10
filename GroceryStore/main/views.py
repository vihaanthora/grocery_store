from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SalesViewSet(viewsets.ModelViewSet):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer
