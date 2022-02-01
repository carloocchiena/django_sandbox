from django import forms

class ReviewForm(forms.Form):
    first_name = forms.CharField(label='First name', max_length=20, required=True)
    last_name = forms.CharField(label='Last name', max_length=20, required=True)
    email = forms.EmailField(label='Email', required=True)
    review = forms.CharField(label='Review', max_length=500, required=True)
    