from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile, Post, comment
from django import forms 

#Create your forms here
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'email')

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True) #This estends UserCreationForm to include email

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['published_date', 'content', 'author', 'title']
    
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def save(self, commit=True):
        review = super().save(commit=False)
        review.user = self.user
        if commit:
            review.save()
        return review
    
class CommentForm(forms.ModelForm):
	class Meta:
		model = comment
		fields = ['post', 'author', 'content', 'created_date', 'updated_date' ]