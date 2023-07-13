from django import forms
from .models import Client
class Clientform(forms.ModelForm):
  class Meta:
    model=Client
    fields=[
      'name', 'cat', 'doe'
    ]
    
