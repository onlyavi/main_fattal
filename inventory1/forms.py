from django import forms
from .models import Stock, SupplierInformation

class StockCreateForm(forms.ModelForm):
    class Meta:
        model=Stock
        #The fields I want to use
        fields=['category_name', 'item_fattal_code', 'item_name', 'quantity_item', 'item_unit_kind','description']
    
    def clean_item_name(self):
        item_name = self.cleaned_data.get('item_name')
        category_name =self.cleaned_data.get('category_name')
        item_fattal_code =self.cleaned_data.get('item_fattal_code')
        if (not category_name) and (not item_name) and (not item_fattal_code) :
            raise forms.ValidationError('You must fill at least one field ITEM CODE or ITEM NAME ')
        #instance = Stock.objects.get(id)
        #print (instance.item_name)
        # if item_name != instance.item_name:
        #     if item_name:                
        for instance in Stock.objects.all():
            if (instance.item_name == item_name):
                raise forms.ValidationError(item_name +' Already exist')
            
        return item_name
    def clean_item_fattal_code(self):
        item_name = self.cleaned_data.get('item_name')
        category_name =self.cleaned_data.get('category_name')
        item_fattal_code =self.cleaned_data.get('item_fattal_code')
        if (not category_name) and (not item_name) and (not item_fattal_code):
            raise forms.ValidationError('You must fill at least one field ITEM CODE or ITEM NAME ')
    
       
    #     if item_fattal_code:
        for instance in Stock.objects.all():    
            if (instance.item_fattal_code == item_fattal_code) and (int(instance.item_fattal_code) < 990000):
                raise forms.ValidationError('item code '+ str(item_fattal_code) +' Already exist')
        return item_fattal_code
    

    
        
class StockSearchForm(forms.ModelForm):
    class Meta:
        model=Stock
        #The fields I want to use
        fields=['category_name','item_name', 'item_fattal_code']
    
    

      
class StockFullSearchForm(forms.ModelForm):
    class Meta:
        model=Stock
        #The fields I want to use
        
        fields=['category_name','item_name','quantity_min','quantity_max','item_fattal_code_begin', 'item_fattal_code_end', 'description']
   
   
    # def clean_item_name(self):
    #     item_name = self.cleaned_data.get('item_name')
    #     if (not item_name):
    #         raise forms.ValidationError('This field is required')
    #     # for instance in Stock.objects.all():
    #     #     if instance.category == category:
    #     #         raise forms.ValidationError(category +' Already exist')
    
    #     return item_name 

   
    
        
class StockUpdateForm(forms.ModelForm):
    class Meta:
        model=Stock
        
        fields=['category_name', 'item_fattal_code', 'item_name', 'quantity_item', 'item_unit_kind','description']
  
  
    # def clean_item_name(self):
    #     item_name = self.cleaned_data.get('item_name')
    #     category_name =self.cleaned_data.get('category_name')
    #     item_fattal_code =self.cleaned_data.get('item_fattal_code')
    #     item_code =self.cleaned_data.get(id)
    #     zz= Stock.objects.values('item_name')
    #     if (not category_name) and (not item_name) and (not item_fattal_code) :
    #         raise forms.ValidationError('You must fill at least one field ITEM CODE or ITEM NAME ')
        
       
        
    #     if item_name and item_fattal_code:                
    #         for instance in Stock.objects.all():
    #             if (instance.item_name == item_name) and (instance.) :
    #                 raise forms.ValidationError(item_name +' Already exist')
    #  else:
    #         if item_name:                
    #             for instance in Stock.objects.all():
    #                 if (instance.item_name == item_name):
    #                     raise forms.ValidationError(item_name +' Already exist')
    #         # 
    #     return item_name
    # 
    # # def clean_item_fattal_code(self):
    #     # item_name = self.cleaned_data.get('item_name')
    #     # category_name =self.cleaned_data.get('category_name')
    #     # item_fattal_code =self.cleaned_data.get('item_fattal_code')
    #     # if (not category_name) and (not item_name) and (not item_fattal_code):
    #         # raise forms.ValidationError('You must fill at least one field ITEM CODE or ITEM NAME ')
    #     # else:
    # #    
    #         # if item_fattal_code:
    #             # for instance in Stock.objects.all():    
    #                 # if (instance.item_fattal_code == item_fattal_code) and (int(instance.item_fattal_code) < 990000):
    #                     # raise forms.ValidationError('item code '+ str(item_fattal_code )+' Already exist')
    #     # return item_fattal_code   





        

class SuppliersCreateForm(forms.ModelForm):
    class Meta:
        model=SupplierInformation
        #The fields I want to use
     #   fields=['suppliers_name','supplier_phone_number','supplier_sale_leader_name','supplier_sale_leader_phone','suppliers_driver_info']
        fields=['suppliers_name']  
