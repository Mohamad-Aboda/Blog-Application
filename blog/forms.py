from django import forms
from django.db.models import fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.models import model_to_dict

from .models import Comment, Post 



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment 
        fields = ("content",)



class SearchForm(forms.Form):
    q = forms.CharField()


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post 
        fields = ['title', 'content',  'category', 'image']



class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post 
        fields = ['title', 'content', 'category', 'image']


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None


    class Meta:
        model = User 
        fields = ['username', 'email', 'password1', 'password2']
       
       
        # doesn't work for password 
        # help_texts = {
        #     'username':None, 
        #     'email':None,
        #     'password':None, 
        #     'password2':None,
        # }

    