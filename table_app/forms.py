from django import forms
from .models import TableData

CATEGORIES = [

]

class DataForm(forms.Form):
    CATEGORIES = forms.CharField(widget = forms.RadioSelect(choices = CATEGORIES))