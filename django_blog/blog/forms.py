from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profile, Post, Comment
from django import forms 
from taggit.forms import TagWidget, TagField

#Create your forms here
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'email')

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True) #This estends UserCreationForm to include email

class PostForm(forms.ModelForm):
    tags = TagField(widget=TagWidget(), required=False)
    class Meta:
        model = Post
        fields = ['published_date', 'content', 'author', 'title','tags']
        widgets = { 'tags': forms.CheckboxSelectMultiple,}
    
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
		model = Comment
		fields = ['post', 'author', 'content', 'created_at', 'updated_at' ]