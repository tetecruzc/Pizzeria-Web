from django import forms
from .models import Pizza

class PizzaForm(forms.ModelForm):

    class Meta:
        model = Pizza
        fields=[
            'ingedients',
            'size',
         #   'user'
        ]
        labels={
            'ingedients': 'Ingredientes',
            'size': 'Tamaño',
          #  'user' : 'Usuario'
        }
        widgets={
            'ingedients': forms.CheckboxSelectMultiple(),
            'size': forms.Select(attrs={'class':'i-dont-know'}),
          #  'user' : forms.Select(attrs={'class':'i-dont-know'})
        }