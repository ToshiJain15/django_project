from django import forms
from .models import HistoricalPerformance

class PerformanceForm(forms.ModelForm):
    class Meta:
        model = HistoricalPerformance
        fields = '__all__'
