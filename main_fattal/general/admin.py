from django.contrib import admin
from .models import  GeneralConfiguration
from .forms import GeneralConfigrationForm
# Register your models here.

   
class GeneralConfigrationAdmin(admin.ModelAdmin):
    class Meta:
        model_gc=GeneralConfiguration
        #The fields I want to use
        list_gc_display=['os_choice','lang_choice', 'gui_choice']
        forms_gc = GeneralConfigrationForm
        list_gc_filter = ['os_choice','lang_choice', 'gui_choice']
        search_gc_fields=['os_choice','lang_choice', 'gui_choice']
       
       

          
    

admin.site.register(GeneralConfiguration,GeneralConfigrationAdmin)



