from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .models import HistoricalPerformance
from .serializers import HistoricalPerformanceSerializer
from rest_framework import generics
from django.shortcuts import render, redirect
from .forms import PerformanceForm
# Create your views here.
class VendorPerformanceAPIView(generics.RetrieveAPIView):
    queryset = HistoricalPerformance.objects.all()
    serializer_class = HistoricalPerformanceSerializer

def performance_form(request):
    if request.method == 'POST':
        form = PerformanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('performance_form.html')  # Redirect to a success page
    else:
        form = PerformanceForm()
    return render(request, 'performance_form.html', {'form': form})
