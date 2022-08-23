from .models import Centers
from django import forms

class CenterForm(forms.ModelForm):

    class Meta:
        model = Centers
        
        fields = "__all__"


        
    
    
    
    