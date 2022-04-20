from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=50, required=False)
    email = forms.EmailField(required=False)
    subject = forms.CharField(max_length=50, required=False)
    phone = forms.CharField(max_length=15, required=False)
    message = forms.Textarea()