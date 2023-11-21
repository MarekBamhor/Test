from django import forms
from models import Person, Family, Relative



class ContactForm(forms.Form):
    Name = forms.CharField(max_length=50)

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

