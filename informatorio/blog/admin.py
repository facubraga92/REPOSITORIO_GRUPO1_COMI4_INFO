from django.contrib import admin
from .models import Post , News , Personal , Titulos , Mision ,Contacto ,RedesSociales
# Register your models here.

admin.site.register(Post),
admin.site.register(News),
admin.site.register(Personal),
admin.site.register(Titulos),
admin.site.register(Mision),
admin.site.register(Contacto),
admin.site.register(RedesSociales)
