from django.shortcuts import render , redirect
from django.views.generic import ListView, DetailView, CreateView , UpdateView ,DeleteView
from .models import Post , News
from django.urls import reverse_lazy

from .forms import PostForm , NewsForm

# Create your views here.

# def inicio(request):
	
# 	return render(request, 'blog/index.html');

class HomeView(ListView):
	model = Post
	template_name='blog/index.html'
	ordering = ['-id']

class ArticleDetailView(DetailView):
	model = Post
	template_name='blog/posteo.html'


class añadir_post(CreateView):
	model = Post
	template_name = 'blog/añadir_post.html'
	form_class = PostForm #
	# fields = '__all__'


class eliminar_post(DeleteView):
	model = Post
	template_name = 'blog/eliminar_post.html'
	success_url = reverse_lazy('inicio')


# def añadir_post(request):
# 	return render(request,'blog/añadir_post.html');

class editar_post(UpdateView):
	model = Post
	template_name = 'blog/editar_post.html'
	form_class = PostForm #
	# fields = ['title','content','epigrafe','image']



def login(request):
	return render(request,'blog/login.html');


def contacto(request):
	return render(request,'blog/contacto.html');


	
def quienessomos(request):
	return render(request,'blog/quienessomos.html');








######################### NOTICIAS  (ESTO ES LO QUE QUIERO INCORPORAR A INDEX.HTML)##############################

## LO ESTABA INTENTANDO INCORPORAR A INDEX.HTML CON UN FOR QUE VAS A ENCONTRAR QUE DICE {% for new  in object_list  %} , TE ACLARO PORQUE HAY VARIOS BUCLES ADENTRO JAJA
class añadir_noticia(CreateView):
	model = News
	template_name = 'blog/añadir_noticia.html'
	form_class = NewsForm #
	# fields = '__all__'



#### aca estaba probando .. no se si es por aca la cosa.. y agregar un context o algo asi ####
class NewsView(ListView):
	model = News
	template_name='blog/index.html'
	ordering = ['-id']



####################################################################