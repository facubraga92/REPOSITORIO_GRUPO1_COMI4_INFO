from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("",views.inicio,name="inicio"),
    path("login/",auth_views.LoginView.as_view(template_name="blog/login.html"),name="login"),
    path("contacto/",views.contacto,name="contacto"),
    path("quienessomos/",views.quienessomos,name="quienessomos"),
    path("logout/", auth_views.logout_then_login , name="logout"),



]