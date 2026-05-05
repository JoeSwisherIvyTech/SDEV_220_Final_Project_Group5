from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        # add what fields the form needs as strings
        fields = {'phone', 'email', 'item', 'alteration_type', 'material', 'description', 'chest', 'waist', 'hips', 'inseam',}