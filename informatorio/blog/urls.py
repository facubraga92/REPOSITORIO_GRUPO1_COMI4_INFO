from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


from .views import HomeView , ArticleDetailView , añadir_post, añadir_noticia , añadir_personal , personal , editar_post, editar_noticia, editar_personal, editar_titulo, editar_mision, editar_contacto, editar_redes , eliminar_post, eliminar_personal, eliminar_noticia ,contactoView ,redes



urlpatterns = [
    # path("",views.inicio,name="inicio"),
    path('',HomeView.as_view(), name='inicio'),
    path('redes/',redes.as_view(), name='redes'),
    path('posteo/<int:pk>/', ArticleDetailView.as_view(),name='detalleposteo'),
    path('contacto/', contactoView.as_view(),name='contacto'),

    path('posteo/edit/<int:pk>/', editar_post.as_view(),name='editar_post'),
    path('edit/<int:pk>/', editar_noticia.as_view(),name='editar_noticia'),
    path('personal/edit/<int:pk>/', editar_personal.as_view(),name='editar_personal'),
    path('titulo/edit/<int:pk>/', editar_titulo.as_view(),name='editar_titulo'),
    path('mision/edit/<int:pk>/', editar_mision.as_view(),name='editar_mision'),
    path('contacto/edit/<int:pk>/', editar_contacto.as_view(),name='editar_contacto'),
    path('redes/edit/<int:pk>/', editar_redes.as_view(),name='editar_redes'),

    path("login/",auth_views.LoginView.as_view(template_name="blog/login.html"),name="login"),
    # path("contacto/",views.contacto,name="contacto"),
    path("quienessomos/",personal.as_view(),name="quienessomos"),
    path("logout/", auth_views.logout_then_login , name="logout"),
    # path('añadir_post/',views.añadir_post,name="añadir_post"),


    path('añadir_post/',añadir_post.as_view(),name='añadir_post'),
    path('añadir_noticia/',añadir_noticia.as_view(),name='añadir_noticia'),
    path('añadir_personal/',añadir_personal.as_view(),name='añadir_personal'),


    path('posteo/<int:pk>/delete', eliminar_post.as_view(),name='eliminar_post'),
    path('noticia/<int:pk>/delete', eliminar_noticia.as_view(),name='eliminar_noticia'),
    path('personal/<int:pk>/delete', eliminar_personal.as_view(),name='eliminar_personal'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)