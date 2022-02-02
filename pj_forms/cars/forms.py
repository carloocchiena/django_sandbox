from django import forms
from .models import Review
from django.forms import ModelForm


# this is the manual\standard way to create a form
# class ReviewForm(forms.Form):
#     first_name = forms.CharField(label='First name', max_length=20, required=True)
#     last_name = forms.CharField(label='Last name', max_length=20, required=True)
#     email = forms.EmailField(label='Email', required=True)
#     review = forms.CharField(label='Review', widget=forms.Textarea(attrs={'class':'mybox'}), required=True)
    
# this is the manual\standard way to create a model form
class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
        