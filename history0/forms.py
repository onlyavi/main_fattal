
from django import forms
from .models import StockHistory

class StockHistoryForm(forms.ModelForm):
    class Meta:
        model=StockHistory
        #The fields I want to use
        fields=['category_nameh', 'item_fattal_codeh', 'item_nameh', 'item_unit_kindh','descriptionh']
    