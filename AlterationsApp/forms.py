from django import forms
from .models import Order
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        # add what fields the form needs as strings
        fields = {'item', 'alteration_type', 'material', 'description', 'chest', 'waist', 'hips', 'inseam',}

# code to extend UserCreationForm from @colinnatjku on medium's "Customizing Django UserCreationForm" article
class RegistrationForm(UserCreationForm):
    # add additional fields
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()

    # include Meta class
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]

class StatusForm(forms.ModelForm):
    status = forms.ChoiceField()

    class Meta:
        model = Order
        fields = {'status',}