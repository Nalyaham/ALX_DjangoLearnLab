from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile

#Create your forms here
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'email')

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True) #This estends UserCreationForm to include email

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']