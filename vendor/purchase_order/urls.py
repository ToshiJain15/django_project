from django.urls import path
from .views import PurchaseOrderListCreateAPIView,PurchaseOrderRetrieveUpdateDestroyAPIView,purchase_order_create

urlpatterns = [
    path('purchase_orders/create/', purchase_order_create, name='purchase-order-create'),
    path('api/purchase_orders/', PurchaseOrderListCreateAPIView.as_view(), name='purchase-order-list-create'),
    path('api/purchase_orders/<int:pk>/', PurchaseOrderRetrieveUpdateDestroyAPIView.as_view(), name='purchase-order-retrieve-update-destroy'),
]