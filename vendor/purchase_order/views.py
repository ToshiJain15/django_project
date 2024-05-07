from rest_framework import generics
from django.shortcuts import render, redirect
from .models import PurchaseOrder
from .serializers import  PurchaseOrderSerializer
from .forms import PurchaseOrderForm


class PurchaseOrderListCreateAPIView(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class PurchaseOrderRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

# purchase_order/views.py
def purchase_order_create(request):
    if request.method == 'POST':
        form = PurchaseOrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('purchase-order-list-create')  # Redirect to the purchase order list page
    else:
        form = PurchaseOrderForm()
    return render(request, 'purchase_order_form.html', {'form': form})
