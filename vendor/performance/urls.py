from django.urls import path
from .views import VendorPerformanceAPIView, performance_form

urlpatterns = [
   path('vendors/<int:pk>/performance/', VendorPerformanceAPIView.as_view(), name='vendor-performance'),
   path('performance/form/', performance_form, name='performance-form'),
]