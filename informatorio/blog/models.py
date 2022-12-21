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
