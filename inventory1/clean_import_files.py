from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import StockCreateForm, SuppliersCreateForm, StockSearchForm,StockUpdateForm, StockFullSearchForm
from .models import *



def clean_excel_item_fattal_code(a,skip):
       # item_name = a.cleaned_data.get('item_name')
        #category_name =self.cleaned_data.get('category_name')
        item_fattal_code =a
          
       
    #     if item_fattal_code:
        for instance in Stock.objects.all():   
            #print (instance.item_fattal_code, " ", type(instance.item_fattal_code) )
            if (str(instance.item_fattal_code) == item_fattal_code) and (int(instance.item_fattal_code) < 990000):
                skip=True
                
                
        return skip
    
def clean_excel_item_name(a,skip):
# item_name = a.cleaned_data.get('item_name')
    #category_name =self.cleaned_data.get('category_name')
    item_name =a
    

#     if item_fattal_code:
    for instance in Stock.objects.all():   
        #print (instance.item_fattal_code, " ", type(instance.item_fattal_code) )
        if instance.item_name == item_name:
            skip=True
            
            
    return skip
def clean_excel_supplliers_name(a,sskip):
# item_name = a.cleaned_data.get('item_name')
    #category_name =self.cleaned_data.get('category_name')
    suppliers_name =a
    

#     if item_fattal_code:
    for instance in SupplierInformation.objects.all():   
        #print (instance.item_fattal_code, " ", type(instance.item_fattal_code) )
        if instance.suppliers_name == a:
            sskip=True
            print ("* found duplicate")
            
    return sskip

