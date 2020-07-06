from django.contrib import admin
from .models import StockHistory
from .forms import StockHistoryForm
# Register your models here.

class StockHistoryAdmin(admin.ModelAdmin):
#BUILTIN ADMIN
# what I want to dis'catagory_name','item_name','item_fattal_code','item_barcode_external','quantity_item'
    list_display = ['category_nameh','item_nameh','item_fattal_codeh','descriptionh' ]
    form = StockHistoryForm
 
    list_filter = ['category_nameh']   #filter items by catagory
    search_fields = ['category_nameh', 'item_nameh']



admin.site.register(StockHistory, StockHistoryAdmin)