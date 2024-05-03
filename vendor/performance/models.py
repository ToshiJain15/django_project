from django.db import models

# Create your models here.
class HistoricalPerformance(models.Model):
  vendor = models.ForeignKey()
  date = models.DateTimeField()
  on_time_delivery_rate = models.FloatField()
  quality_rating_avg = models.FloatField()
  average_response_time = models.FloatField()
  fulfillment_rate = models.FloatField()