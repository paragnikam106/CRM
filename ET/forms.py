from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Tracking

from django import forms

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput , TextInput


# register/ create a user
class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1','password2']

# Create a login form
class LoginForm(AuthenticationForm):
    class Meta:
        username = forms.CharField(widget=TextInput)
        password = forms.CharField(widget=PasswordInput)
    

#create employee record
class AddRecord(forms.ModelForm):
    class Meta:
        model=Tracking
        fields=['first_name','last_name','amount','category','note']

#Update record
class UpdateRecordForm(forms.ModelForm):
    class Meta:
        model= Tracking
        fields=['first_name','last_name','amount','category','note']