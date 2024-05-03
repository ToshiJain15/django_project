from django.db import models

# Create your models here.
class PurchaseOrder(models.Model):
  po_number = models.CharField(max_length=255)
  vendor = models.ForeignKey()
  order_date = models.DateTimeField()
  delivery_date = models.DateTimeField()
  items = models.JSONField()
  quantity = models.IntegerField()
  status = models.CharField(max_length=255)
  quality_rating = models.FloatField()
  issue_date = models.DateTimeField()
  acknowledgement_date = models.DateTimeField()
