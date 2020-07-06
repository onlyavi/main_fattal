from django.db import models

# Create your models here.

class StockHistory(models.Model):
    
    category_nameh = models.CharField(max_length=50, blank=True, null=True) 
    sub_category_nameh = models.CharField(max_length=50, blank=True, null=True) 
    item_nameh = models.CharField(max_length=50, blank=True, null=True)
    item_unit_kind_choiceh={
        ('kg','kg'),
        ('grams','grams'), 
        ('liters','liters'),
        ('units in box','unit_in_box'),
        ('other','other'),
    }
    
    item_unit_kindh=models.CharField(max_length=50, blank=True, null=True, choices=item_unit_kind_choiceh)  #blank=False a must to use
    item_transferh_toh=models.CharField(max_length=50, blank=True, null=True)
    item_transferh_quantityh=models.CharField(max_length=50,blank=True, null=True)
    descriptionh=models.CharField(max_length=50, blank=True, null=True)
    imageh=models.ImageField(upload_to='images/')  
    item_fattal_codeh= models.DecimalField(default='0',decimal_places=0,max_digits=1000,blank=True)
    item_fattal_code_beginh= models.DecimalField(default='-1',decimal_places=0,max_digits=1000,blank=False)
    item_fattal_code_endh= models.DecimalField(default='9999999999',decimal_places=0,max_digits=1000,blank=False)
    commenth=models.CharField(max_length=50, blank=True, null=True)
    transfer_towhomh=models.CharField(max_length=50, blank=True, null=True)