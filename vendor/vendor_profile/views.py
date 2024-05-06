from rest_framework import generics
from .models import Vendor
from .serializers import VendorSerializer
from django.shortcuts import render, redirect
from .forms import VendorForm

class VendorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class VendorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


def vendor_create(request):
    if request.method == 'POST':
        form = VendorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vendor-list-create')  
    else:
        form = VendorForm()
    return render(request, 'vendor_form.html', {'form': form})