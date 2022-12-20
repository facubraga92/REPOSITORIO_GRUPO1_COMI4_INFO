from django.urls import path
from . import views

urlpatterns = [
    path("",views.inicio,name="inicio"),
    path("login/",views.login,name="login"),
    path("contacto/",views.contacto,name="contacto"),
    path("quienessomos/",views.quienessomos,name="quienessomos"),



]