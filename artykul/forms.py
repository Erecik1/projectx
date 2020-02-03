from django import forms
import artykul
from artykul.models import Artykul

class ArtykulSearchForm(forms.Form):
    title = forms.CharField(required=False,
                             label="Tytul",
                             max_length=8)
    
    autor = forms.CharField(required=False,
                             label="Autor",
                             max_length=15)
    
    tresc = forms.CharField(required=False,
                             label="Tresc",
                             max_length=23)
    
class ArtykulForm(forms.ModelForm):
    
    class Meta:
        model = Artykul
        fields = ("tytul",
                  "opis",
                  "file",
                  "data_publikacji")