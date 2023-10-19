from django import forms

class ContactForm(forms.Form):
    Name = forms.CharField(max_length=50)

