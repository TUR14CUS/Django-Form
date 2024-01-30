from django import forms


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    phone = forms.CharField(max_length=15)
    date = forms.DateTimeField(auto_now_add=True)
    occupation = forms.CharField(max_length=80)