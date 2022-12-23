from django.db import models
from django.contrib.auth.models import User #esto ya viene predefinido por django
from django.utils import timezone #idem anterior
from django.urls import reverse


# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length= 255)
    timestamp = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    epigrafe = models.TextField(default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name= 'posts')
    image = models.ImageField(null=True,blank=True,upload_to='media/')
    
       #importar os en settings.py e instalar en cmd "pip install pillow" y hacer migrations.
    
    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return reverse('detalleposteo',args = (str(self.id)))
        return reverse('inicio')



class News(models.Model):
    title = models.CharField(max_length= 255)
    timestamp = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name= 'news')
    image = models.ImageField(null=True,blank=True,upload_to='media/')
    
       #importar os en settings.py e instalar en cmd "pip install pillow" y hacer migrations.
    
    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return reverse('detalleposteo',args = (str(self.id)))
        return reverse('inicio')



class Personal(models.Model):
    NombreCompleto = models.CharField(max_length= 255)
    Descripcion = models.CharField(max_length= 255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name= 'persona')
    image = models.ImageField(null=True,blank=True,upload_to='media/')

       #importar os en settings.py e instalar en cmd "pip install pillow" y hacer migrations.
    
    
    def __str__(self):
        return self.NombreCompleto

    def get_absolute_url(self):
        # return reverse('detalleposteo',args = (str(self.id)))
        return reverse('quienessomos')


class Titulos(models.Model):
    titulo = models.CharField(max_length= 255 , default='Titulo')
    subtitulo = models.CharField(max_length= 255 , default= 'Subtitulo')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name= 'titulos' , default='admin')
    
       #importar os en settings.py e instalar en cmd "pip install pillow" y hacer migrations.
    
    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        # return reverse('detalleposteo',args = (str(self.id)))
        return reverse('inicio')




class Mision(models.Model):
    titulo = models.CharField(max_length= 255)
    subtitulo = models.CharField(max_length= 255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name= 'mision')
    
       #importar os en settings.py e instalar en cmd "pip install pillow" y hacer migrations.
    
    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        # return reverse('detalleposteo',args = (str(self.id)))
        return reverse('inicio')



class RedesSociales(models.Model):
    nombreRedSocial = models.CharField(max_length= 255)
    link = models.URLField(max_length= 255)
    
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name= 'mision')
    
       #importar os en settings.py e instalar en cmd "pip install pillow" y hacer migrations.
    
    def __str__(self):
        return self.nombreRedSocial
    def get_absolute_url(self):
        # return reverse('detalleposteo',args = (str(self.id)))
        return reverse('redes')




    
class Contacto(models.Model):
    titulo = models.CharField(max_length= 255)
    descripcion = models.TextField(max_length= 255)
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name= 'mision')
    
       #importar os en settings.py e instalar en cmd "pip install pillow" y hacer migrations.
    
    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        # return reverse('detalleposteo',args = (str(self.id)))
        return reverse('contacto')
    
    