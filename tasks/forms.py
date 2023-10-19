from django import forms
from .models import IceCream, MyModel

class IceCreamForm(forms.ModelForm):
    class Meta:
        model = IceCream
        fields = ['flavor', 'description', 'price']
        labels = {
            'flavor': 'Вкус мороженого',
            'description': 'Описание мороженого',
            'price': 'Цена',
        }

class MyForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ['name', 'email']