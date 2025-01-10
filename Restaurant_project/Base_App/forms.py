# forms.py
from django import forms
from Base_App.models import BookTable,feedback
from django.contrib.auth.forms import UserCreationForm


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = feedback
        fields = ['user_name','Rating','Message','c_image']
        widgets = {
            'user_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Name'}),
            'Rating':forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter your Rating'}),
            'Message':forms.Textarea(attrs={'class':'form-control','placeholder':'Enter your Message'}),
            'c_image':forms.FileInput(attrs={'class':'form-control'}),
        }
        
class RegitsterForm(UserCreationForm):
    email = forms.EmailField(required=False)
    class Meta:
        fields = ['username','email','password1','password2']
        
        