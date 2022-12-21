from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


from .views import HomeView , ArticleDetailView , añadir_post , editar_post , eliminar_post



urlpatterns = [
    # path("",views.inicio,name="inicio"),
    path('',HomeView.as_view(), name='inicio'),
    path('posteo/<int:pk>/', ArticleDetailView.as_view(),name='detalleposteo'),

    path('posteo/edit/<int:pk>/', editar_post.as_view(),name='editar_post'),

    path("login/",auth_views.LoginView.as_view(template_name="blog/login.html"),name="login"),
    path("contacto/",views.contacto,name="contacto"),
    path("quienessomos/",views.quienessomos,name="quienessomos"),
    path("logout/", auth_views.logout_then_login , name="logout"),
    # path('añadir_post/',views.añadir_post,name="añadir_post"),
    path('añadir_post/',añadir_post.as_view(),name='añadir_post'),

    path('posteo/<int:pk>/delete', eliminar_post.as_view(),name='eliminar_post'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)