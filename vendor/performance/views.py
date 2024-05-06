from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import HistoricalPerformance
from .serializers import HistoricalPerformanceSerializer

# Create your views here.
class VendorPerformanceAPIView(generics.RetrieveAPIView):
    queryset = HistoricalPerformance.objects.all()
    serializer_class = HistoricalPerformanceSerializer