# from cProfile import label
# from email.policy import default
# from logging import PlaceHolder
# from django import forms
# from django.forms import CheckboxInput, TextInput,EmailInput,NumberInput,PasswordInput,BooleanField
# from django.contrib.auth import get_user_model
# from django.contrib.auth.forms import UserCreationForm
# from django.forms import ModelForm

# from base.models import Profile



# from django.forms import 
# from .models import User

# class RForm(UserCreationForm):
#     first_name = forms.CharField(widget=TextInput(attrs={'label':'First Name', 'placeholder':'First Name' }))
#     last_name = forms.CharField(widget=TextInput(attrs={'label':'Last Name', 'placeholder':'Last Name' }))
#     college = forms.CharField(widget=TextInput(attrs={'label':'College', 'placeholder':'College' }))
#     program = forms.CharField(widget=TextInput(attrs={'label':'Program', 'placeholder':'Program' }))
#     department = forms.CharField(widget=TextInput(attrs={'label':'Department', 'placeholder':'Department' }))
#     year = forms.CharField(widget=TextInput(attrs={'label':'Year', 'placeholder':'Year' }))
#     email = forms.EmailField(widget=EmailInput(attrs={'label':'Email', 'placeholder':'Email' }))
#     phone_no = forms.IntegerField(widget=NumberInput(attrs={'label':'Phone No.', 'placeholder':'Phone No.' }))
#     password1 = forms.CharField(widget=PasswordInput(attrs={'label':'Set Password', 'placeholder':'Set Password' }))
#     password2 = forms.CharField(widget=PasswordInput(attrs={'label':'Confirm Password', 'placeholder':'Confirm Password' }))
#     gender = forms.BooleanField()

#     class Meta:
#         model = get_user_model()
#         exclude = ['created_at']


from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile

# from django.forms import 
# from .models import User

class RForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields= ['first_name','last_name','email', 'phone_no','staff']

class Form2(forms.ModelForm):
    class Meta:
        model = Profile
        fields= ['college','program','department', 'year']