from django import forms
from .models import Post,News


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','timestamp','content','epigrafe','user','image']

        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control' }),
            'timestamp' : forms.HiddenInput(attrs={'class' : 'form-control' }),
            'content' : forms.Textarea(attrs={'class' : 'form-control' }),
            'epigrafe' : forms.TextInput(attrs={'class' : 'form-control' }),
            'user' : forms.Select(attrs={'class' : 'form-control' }),
            'image' : forms.ClearableFileInput(attrs={'class' : 'form-control'})
        }


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title','timestamp','content','user','image']

        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control' }),
            'timestamp' : forms.HiddenInput(attrs={'class' : 'form-control' }),
            'content' : forms.Textarea(attrs={'class' : 'form-control' }),
            'user' : forms.Select(attrs={'class' : 'form-control' }),
            'image' : forms.ClearableFileInput(attrs={'class' : 'form-control'})
        }