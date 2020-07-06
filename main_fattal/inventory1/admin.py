from django.contrib import admin
from .models import Stock, SupplierInformation, Job
from .forms import StockCreateForm, SuppliersCreateForm
# Register your models here.


class StockCreateAdmin(admin.ModelAdmin):
#BUILTIN ADMIN
# what I want to dis'catagory_name','item_name','item_fattal_code','item_barcode_external','quantity_item'
    list_display = ['category_name','item_name','item_fattal_code','item_barcode_external','quantity_item', 'item_fattal_code_issue','description' ]
    form = StockCreateForm
 
    list_filter = ['category_name']   #filter items by catagory
    search_fields = ['category_name', 'item_name']


class SuppliersCreateAdmin(admin.ModelAdmin):
#BUILTIN ADMIN
# what I want to dis'catagory_name','item_name','item_fattal_code','item_barcode_external','quantity_item'
    # list_display = ['suppliers_name','supplier_phone_number','supplier_sale_leader_name','supplier_sale_leader_phone','suppliers_driver_info']
    # form = SuppliersCreateForm
 
    # list_filter = ['suppliers_name']   #filter items by catagory
    # search_fields =['suppliers_name','supplier_phone_number','supplier_sale_leader_name','supplier_sale_leader_phone','suppliers_driver_info']
    list_display2 = ['suppliers_name']
    form2 = SuppliersCreateForm
 
    list_filter2 = ['suppliers_name']   #filter items by catagory
    search_fields2 =['suppliers_name']

    
    
admin.site.register(Stock, StockCreateAdmin)
admin.site.register(SupplierInformation, SuppliersCreateAdmin)
admin.site.register(Job)





 

