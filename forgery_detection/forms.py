# forms.py 
from django import forms 
from .models import *
  
class databaseForm(forms.ModelForm): 
  
    class Meta: 
        model = database 
        fields = ['Please_Select_Image_to_Detect_Forgery'] 