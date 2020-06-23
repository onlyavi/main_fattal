from django.db import models

# Create your models here.




class Stock(models.Model):
    
    category_name = models.CharField(max_length=50, blank=True, null=True) 
    sub_category_name = models.CharField(max_length=50, blank=True, null=True) 
    item_name = models.CharField(max_length=50, blank=True, null=True)
   # item_fattal_code=models.CharField(max_length=50, blank=True, null=True)
    item_fattal_code= models.DecimalField(default='0',decimal_places=0,max_digits=1000,blank=True)
    item_fattal_code_begin= models.DecimalField(default='-1',decimal_places=0,max_digits=1000,blank=False)
    item_fattal_code_end= models.DecimalField(default='9999999999',decimal_places=0,max_digits=1000,blank=False)
    item_barcode_external = models.CharField(max_length=50, blank=True, null=True)
    item_unit_kind_choice={
        ('kg','kg'),
        ('grams','grams'), 
        ('liters','liters'),
        ('units in box','unit_in_box'),
        ('other','other'),
    }
    
    item_unit_kind=models.CharField(max_length=50, blank=True, null=True, choices=item_unit_kind_choice)  #blank=False a must to use
    
    quantity_item= models.DecimalField(default='0',decimal_places=0,max_digits=1000,blank=True)
    quantity_min= models.DecimalField(default='0',decimal_places=0,max_digits=1000,blank=False)
    quantity_max= models.DecimalField(default='999999999',decimal_places=0,max_digits=1000,blank=False)

    hotel_name_transfer=models.CharField (max_length=50, blank=True, null=True)
    hotel_quantity_transfer=models.IntegerField(default='0', blank=True, null=True)
    item_transfer_to=models.CharField(max_length=50, blank=True, null=True)
    item_transfer_quantity=models.CharField(max_length=50,blank=True, null=True)
    alchol_color=models.CharField(max_length=50, blank=True,null=True)
    alchol_kind=models.CharField(max_length=50,blank=True, null=True)
    description=models.CharField(max_length=50, blank=True, null=True)
    export_to_CSV = models.BooleanField(default=False)
    suppliers_unit_kind_choice={
        ('kg','kg'),
        ('grams','grams'),
        ('liters','liters'),
        ('units in box','unit_in_box'),
        ('other','other'),
    }
    
    suppliers_item_unit_kind=models.CharField(max_length=50, blank=True, null=True, choices=suppliers_unit_kind_choice)
    suppliers_fattal_code=models.CharField(max_length=50, blank=True, null=True, choices=suppliers_unit_kind_choice)
  
    image=models.ImageField(upload_to='images/')  
    
    
    
    

    
class SupplierInformation(models.Model):
    # suppliers_choice ={
    #     ('a','a'),
    #     ('b','b'),
    #     ('c','c'),
    #     ('other','other')        
    # }
    # suppliers_name=models.CharField(max_length=50, blank=True, null=True, choices=suppliers_choice)
    suppliers_name = models.CharField(max_length=50, blank=True, null=True)
    suppliers_item_unit_quantity=models.DecimalField(default='0',decimal_places=0,max_digits=1000,blank=True)
    
    suppliers_sale_leader_name=models.CharField (max_length=50, blank=True, null=True)
    suppliers_sale_leader_phone=models.CharField (max_length=50, blank=True, null=True)
    suppliers_drivers_info=models.CharField (max_length=50, blank=True, null=True) 
    suppliers_phone_number=models.CharField (max_length=50, blank=True, null=True)
    

class Job(models.Model):
    image=models.ImageField(upload_to='images/')                          
    summery = models.CharField(max_length=200)




#sample
# category = models.CharField(max_length=50, blank=True, null=True)  #blank=False a must to use
# export_to_CSV = models.BooleanField(default=False)
# display_heb = models.BooleanField(default=False)
# quantity = models.IntegerField(default='0', blank=True, null=True)
# suppliers_choice = {
#             ('Avivi','Avivi'),
#             ('Neto','Neto'),
#             ('Acadmy Lebaser','Acadmy Lebaser'),
#             ('Bisqoti','Bisqoti'),
#             ('Tavlini Hagit','Tavlini Hagit'),
#             ('other','other'),
     
#         }
#     suppliers_name = models.CharField(max_length=50, blank=True, null=True, choices=suppliers_choice)
                                      
#     def __str__(self):
#         #I need to put the arguments  togther (string+int), but also to add space, so in the future I can split it.
#         return self.item_name + ' ' + str(self.quantity)

