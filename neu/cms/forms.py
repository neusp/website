from django import forms
from models import Person

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Person
