from django.urls import path
from .views import VendorPerformanceAPIView, performance_form, HistoricalPerformanceListCreateAPIView

urlpatterns = [
   path('vendors/<int:pk>/performance/', VendorPerformanceAPIView.as_view(), name='vendor-performance'),
   path('api/performance/',HistoricalPerformanceListCreateAPIView.as_view(), name='performance-list'),
    
   path('performance/form/', performance_form, name='performance-form'),
]