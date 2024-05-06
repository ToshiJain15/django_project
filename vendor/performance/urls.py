from django.urls import path
from .views import VendorPerformanceAPIView

urlpatterns = [
   path('vendors/<int:pk>/performance/', VendorPerformanceAPIView.as_view(), name='vendor-performance'),
]