from django import forms
from django.forms import ModelForm
from .models import Review

# this is the manual\standard way to create a form
# class ReviewForm(forms.Form):
#     first_name = forms.CharField(label='First name', max_length=20, required=True)
#     last_name = forms.CharField(label='Last name', max_length=20, required=True)
#     email = forms.EmailField(label='Email', required=True)
#     review = forms.CharField(label='Review', widget=forms.Textarea(attrs={'class':'mybox'}), required=True)
    
# this is the way to create a model form with Django Classes
class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
        
        # add here your custom labels for the forms
        labels = {
            'first_name': 'First name',
            'last_name': 'Last name',
        }
        
        # add here your custom error messages for the forms
        error_messages = {
            'stars': {
                'min_value': 'Please enter a value greater than or equal to 1.',
                'max_value': 'Please enter a value less than or equal to 5.'
            }
        }
        