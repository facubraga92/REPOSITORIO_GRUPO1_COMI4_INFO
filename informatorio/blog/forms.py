from django import forms
from .models import Post,News,Personal , Titulos , Mision , Contacto , RedesSociales


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

class PersonalForm(forms.ModelForm):
    class Meta:
        model = Personal
        fields = ['NombreCompleto','Descripcion','user','image']

        widgets = {
            'NombreCompleto' : forms.TextInput(attrs={'class' : 'form-control' }),
            'Descripcion' : forms.Textarea(attrs={'class' : 'form-control' }),
            'user' : forms.Select(attrs={'class' : 'form-control' }),
            'image' : forms.ClearableFileInput(attrs={'class' : 'form-control'})
        }





class TitulosForm(forms.ModelForm):
    class Meta:
        model = Titulos
        fields = ['titulo','subtitulo','user']

        widgets = {
            'titulo' : forms.TextInput(attrs={'class' : 'form-control' }),
            'subtitulo' : forms.Textarea(attrs={'class' : 'form-control' }),
            'user' : forms.Select(attrs={'class' : 'form-control' }),
        }


class MisionForm(forms.ModelForm):
    class Meta:
        model = Mision
        fields = ['titulo','subtitulo','user']

        widgets = {
            'titulo' : forms.TextInput(attrs={'class' : 'form-control' }),
            'subtitulo' : forms.Textarea(attrs={'class' : 'form-control' }),
            'user' : forms.Select(attrs={'class' : 'form-control' }),
        }



class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['titulo','descripcion']

        widgets = {
            'titulo' : forms.TextInput(attrs={'class' : 'form-control' }),
            'descripcion' : forms.Textarea(attrs={'class' : 'form-control' }),
            # 'user' : forms.Select(attrs={'class' : 'form-control' }),
        }


class RedesSocialesForm(forms.ModelForm):
    class Meta:
        model = RedesSociales
        fields = ['nombreRedSocial','link']

        widgets = {
            'nombreRedSocial' : forms.TextInput(attrs={'class' : 'form-control' }),
            'link' : forms.TextInput(attrs={'class' : 'form-control' })
            # 'user' : forms.Select(attrs={'class' : 'form-control' }),
        }