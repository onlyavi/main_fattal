from django.db import models

# Create your models here.
class GeneralConfiguration(models.Model):
    os_choice={
        ('windows','windows'),
        ('linux','linux'),
        
    }
    os= models.CharField(max_length=50, blank=True, null=True, choices=os_choice)
    lang_choice={
        ('english','english'),
        ('eng_heb','engl_heb'),
        ('full_hebrew','full_hebrew'),
    }
    lang= models.CharField(max_length=50, blank=True, null=True, choices=lang_choice)
    gui_choice={
        ('web','web'),
        ('Tkinter','Tkinter'),
    }
    gui_kind= models.CharField(max_length=50, blank=True, null=True, choices=gui_choice)
    
        
def __config__(self):
    #I need to put the arguments  togther (string+int), but also to add space, 
    # so in the future I can split it.

    return self.os
    

                  




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


from django.db import models

# Create your models here.
class Stock(models.Model):
    category_name = models.CharField(max_length=50, blank=True, null=True)  #blank=False a must to use
    item_name = models.CharField(max_length=80, blank=True, null=True)
    item_fattal_code=models.CharField (max_length=50,blank=True, null=True)
    item_barcode_external = models.CharField(max_length=50, blank=True, null=True)
    quantity_item= models.IntegerField(default='0',blank=True,null=True)
    suppliers_choice ={
        ('a','a'),
        ('b','b'),
        ('c','c'),
        ('other','other')        
    }
    suppliers_name=models.CharField(max_length=50, blank=True, null=True, choices=suppliers_choice)
    hotel_name_transfer=models.CharField (max_length=50, blank=True, null=True)
    hotel_quantity_transfer=models.IntegerField(default='0', blank=True, null=True)
    item_transfer_to=models.CharField(max_length=50, blank=True, null=True)
    item_transfer_quantity=models.CharField(max_length=50,blank=True, null=True)
    alchol_color=models.CharField(max_length=50, blank=True,null=True)
    alchol_kind=models.CharField(max_length=50,blank=True, null=True)
    details=models.CharField(max_length=100, blank=True, null=True)
    export_to_CSV = models.BooleanField(default=False)
    
    
    def __str__(self):
        #I need to put the arguments  togther (string+int), but also to add space, 
        # so in the future I can split it.
      
        return self.item_name + ' ' + str(self.quantity_item)


class GeneralConfiguration(models.Model):
    os_choice={
        ('windows','windows'),
        ('linux','linux'),
        
    }
    os= models.CharField(max_length=50, blank=True, null=True, choices=os_choice)
    lang_choice={
        ('english','english'),
        ('eng_heb','engl_heb'),
        ('full_hebrew','full_hebrew'),
    }
    lang= models.CharField(max_length=50, blank=True, null=True, choices=lang_choice)
    gui_choice={
        ('web','web'),
        ('Tkinter','Tkinter'),
    }
    gui_kind= models.CharField(max_length=50, blank=True, null=True, choices=gui_choice)
    
        
def __config__(self):
    #I need to put the arguments  togther (string+int), but also to add space, 
    # so in the future I can split it.

    return self.os
    


                             




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


from django.db import models

# Create your models here.
class Stock(models.Model):
    category_name = models.CharField(max_length=50, blank=True, null=True)  #blank=False a must to use
    item_name = models.CharField(max_length=80, blank=True, null=True)
    item_fattal_code=models.CharField (max_length=50,blank=True, null=True)
    item_barcode_external = models.CharField(max_length=50, blank=True, null=True)
    quantity_item= models.IntegerField(default='0',blank=True,null=True)
    suppliers_choice ={
        ('a','a'),
        ('b','b'),
        ('c','c'),
        ('other','other')        
    }
    suppliers_name=models.CharField(max_length=50, blank=True, null=True, choices=suppliers_choice)
    hotel_name_transfer=models.CharField (max_length=50, blank=True, null=True)
    hotel_quantity_transfer=models.IntegerField(default='0', blank=True, null=True)
    item_transfer_to=models.CharField(max_length=50, blank=True, null=True)
    item_transfer_quantity=models.CharField(max_length=50,blank=True, null=True)
    alchol_color=models.CharField(max_length=50, blank=True,null=True)
    alchol_kind=models.CharField(max_length=50,blank=True, null=True)
    details=models.CharField(max_length=100, blank=True, null=True)
    export_to_CSV = models.BooleanField(default=False)
    
    
    def __str__(self):
        #I need to put the arguments  togther (string+int), but also to add space, 
        # so in the future I can split it.
      
        return self.item_name + ' ' + str(self.quantity_item)


class GeneralConfiguration(models.Model):
    os_choice={
        ('windows','windows'),
        ('linux','linux'),
        
    }
    os= models.CharField(max_length=50, blank=True, null=True, choices=os_choice)
    lang_choice={
        ('english','english'),
        ('eng_heb','engl_heb'),
        ('full_hebrew','full_hebrew'),
    }
    lang= models.CharField(max_length=50, blank=True, null=True, choices=lang_choice)
    gui_choice={
        ('web','web'),
        ('Tkinter','Tkinter'),
    }
    gui_kind= models.CharField(max_length=50, blank=True, null=True, choices=gui_choice)
    
        
def __config__(self):
    #I need to put the arguments  togther (string+int), but also to add space, 
    # so in the future I can split it.

    return self.os
    


                             




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


from django.db import models

# Create your models here.
class Stock(models.Model):
    category_name = models.CharField(max_length=50, blank=True, null=True)  #blank=False a must to use
    item_name = models.CharField(max_length=80, blank=True, null=True)
    item_fattal_code=models.CharField (max_length=50,blank=True, null=True)
    item_barcode_external = models.CharField(max_length=50, blank=True, null=True)
    quantity_item= models.IntegerField(default='0',blank=True,null=True)
    suppliers_choice ={
        ('a','a'),
        ('b','b'),
        ('c','c'),
        ('other','other')        
    }
    suppliers_name=models.CharField(max_length=50, blank=True, null=True, choices=suppliers_choice)
    hotel_name_transfer=models.CharField (max_length=50, blank=True, null=True)
    hotel_quantity_transfer=models.IntegerField(default='0', blank=True, null=True)
    item_transfer_to=models.CharField(max_length=50, blank=True, null=True)
    item_transfer_quantity=models.CharField(max_length=50,blank=True, null=True)
    alchol_color=models.CharField(max_length=50, blank=True,null=True)
    alchol_kind=models.CharField(max_length=50,blank=True, null=True)
    details=models.CharField(max_length=100, blank=True, null=True)
    export_to_CSV = models.BooleanField(default=False)
    
    
    def __str__(self):
        #I need to put the arguments  togther (string+int), but also to add space, 
        # so in the future I can split it.
      
        return self.item_name + ' ' + str(self.quantity_item)


class GeneralConfiguration(models.Model):
    os_choice={
        ('windows','windows'),
        ('linux','linux'),
        
    }
    os= models.CharField(max_length=50, blank=True, null=True, choices=os_choice)
    lang_choice={
        ('english','english'),
        ('eng_heb','engl_heb'),
        ('full_hebrew','full_hebrew'),
    }
    lang= models.CharField(max_length=50, blank=True, null=True, choices=lang_choice)
    gui_choice={
        ('web','web'),
        ('Tkinter','Tkinter'),
    }
    gui_kind= models.CharField(max_length=50, blank=True, null=True, choices=gui_choice)
    
        
def __config__(self):
    #I need to put the arguments  togther (string+int), but also to add space, 
    # so in the future I can split it.

    return self.os
    


                             




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

