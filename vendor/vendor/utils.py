from django.db.models import Count, Avg, F
from vendor_profile.models import Vendor
from purchase_order.models import PurchaseOrder

def calculate_performance_metrics(vendor):
    # On-Time Delivery Rate
    completed_orders = vendor.purchaseorder_set.filter(status='completed')
    on_time_orders = completed_orders.filter(delivery_date__lte=F('vendor__delivery_date'))
    vendor.on_time_delivery_rate = (on_time_orders.count() / completed_orders.count()) * 100 if completed_orders.count() else 0

    # Quality Rating Average
    vendor.quality_rating_avg = completed_orders.aggregate(Avg('quality_rating'))['quality_rating__avg'] or 0

    # Average Response Time
    acknowledged_orders = completed_orders.exclude(acknowledgment_date=None)
    vendor.average_response_time = acknowledged_orders.aggregate(Avg(F('acknowledgment_date') - F('issue_date')))['acknowledgment_date__avg'].total_seconds() if acknowledged_orders.count() else 0

    # Fulfillment Rate
    vendor.fulfillment_rate = (completed_orders.exclude(status='completed with issues').count() / completed_orders.count()) * 100 if completed_orders.count() else 0

    vendor.save()
