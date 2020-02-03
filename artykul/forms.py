from django import forms
import artykul
from artykul.models import Artykul

class ArtykulSearchForm(forms.Form):
    title = forms.CharField(required=False,
                             label="Tytul",
                             max_length=8)

    description = forms.CharField(required=False,
                             label="Tresc",
                             max_length=23)
    
class ArtykulForm(forms.ModelForm):
    
    class Meta:
        model = Artykul
        fields = ("Title",
                  "Description",
                  "File",
                  "Date",)