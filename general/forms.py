from django import forms
from .models import GeneralConfiguration

class GeneralConfigrationForm(forms.ModelForm):
    class Meta:
        model_gc=GeneralConfiguration
        #The fields I want to use
        fields_gc=['os_choice','lang_choice', 'gui_choice']
        
    
        