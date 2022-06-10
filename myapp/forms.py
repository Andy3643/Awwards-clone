from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class UserRegisterForm(UserCreationForm):
    '''
    Adds more fields to user creation form
    '''
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class UserUpdateForm(forms.ModelForm):
    '''
    Form to update user profile
    '''
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email']

class ProfileUpdateForm(forms.ModelForm):
    '''
    Form to update user profile picture
    '''
    class Meta:
        model = Profile
        fields = ['bio','profile_pic']
        
class ProjectUploadForm(forms.ModelForm):
    '''
    Form to allow users upload project.
    '''
    class Meta:
        model = Project
        fields = ["title","description","link","image"]



