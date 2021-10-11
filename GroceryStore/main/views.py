from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from .serializers import *
from .models import *
import datetime
from rest_framework import status

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SalesViewSet(viewsets.ModelViewSet):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer

class MonthlyPurchaseViewSet(viewsets.ViewSet):

    def retrieve(self, request, pk=None):
        current_month = datetime.datetime.today().month
        queryset = Sales.objects.filter(user=pk, date__month=current_month)
        serializer = SalesSerializer(queryset, many=True)
        return Response(serializer.data)

    def list(self, request):
        current_month = datetime.datetime.today().month
        queryset = Sales.objects.filter(date__month=current_month)
        serializer = SalesSerializer(queryset, many=True)
        return Response(serializer.data)