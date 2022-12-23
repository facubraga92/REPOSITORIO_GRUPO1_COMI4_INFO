from django.shortcuts import render , redirect
from django.views.generic import ListView, DetailView, CreateView , UpdateView ,DeleteView
from .models import Post , News , Personal , Titulos , Mision , Contacto , RedesSociales
from django.urls import reverse_lazy

from .forms import PostForm , NewsForm , PersonalForm , TitulosForm , MisionForm , ContactoForm , RedesSocialesForm

# Create your views here.

# def inicio(request):
	
# 	return render(request, 'blog/index.html');



######################### POSTEOS ##############################


class HomeView(ListView):
	model = Post
	template_name='blog/index.html'
	ordering = ['-id']
##ESTO DE ABAJO ES PARA AGREGAR MAS CONTEXTOS A UNA MISMA TEMPLATE.
	def get_context_data(self, **kwargs):
		context = super(HomeView,self).get_context_data(**kwargs)
		context.update({
			'noticias' : News.objects.order_by('-timestamp'),
			'titulos' : Titulos.objects.order_by('id'),
			'mision' : Mision.objects.all(),
			'redesSociales' : RedesSociales.objects.all()
		})
		return context

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


	
# def quienessomos(request):
# 	return render(request,'blog/quienessomos.html');








######################### NOTICIAS##############################

class añadir_noticia(CreateView):
	model = News
	template_name = 'blog/añadir_noticia.html'
	form_class = NewsForm #
	# fields = '__all__'



class editar_noticia(UpdateView):
	model = News
	template_name = 'blog/editar_noticia.html'
	form_class = NewsForm #
	# fields = ['title','content','epigrafe','image']


class eliminar_noticia(DeleteView):
	model = News
	template_name = 'blog/eliminar_noticia.html'
	success_url = reverse_lazy('inicio')

# class verNoticia(ListView):
# 	model = News
# 	template_name='blog/eliminar_noticia.html'
# 	ordering = ['-id']

# 	def get_context_data(self, **kwargs):
# 		context = super(verNoticiaEliminar,self).get_context_data(**kwargs)
# 		context.update({
# 			'noticias' : News.objects.order_by('timestamp'),
# 		})
# 		return context
	



######################### PERSONAL ##############################
class añadir_personal(CreateView):
	model = Personal
	template_name = 'blog/añadir_personal.html'
	form_class = PersonalForm #
	# fields = '__all__'

class personal(ListView):
	model = Personal
	template_name='blog/quienessomos.html'
	ordering = ['id']

class eliminar_personal(DeleteView):
	model = Personal
	template_name = 'blog/eliminar_personal.html'
	success_url = reverse_lazy('quienessomos')

class editar_personal(UpdateView):
	model = Personal
	template_name = 'blog/editar_personal.html'
	form_class = PersonalForm #
	# fields = ['title','content','epigrafe','image']




######################### TITULO ##############################


class editar_titulo(UpdateView):
	model = Titulos
	template_name = 'blog/editar_titulo.html'
	form_class = TitulosForm #
	# fields = ['title','content','epigrafe','image']



######################### MISION ##############################

class editar_mision(UpdateView):
	model = Mision
	template_name = 'blog/editar_mision.html'
	form_class = MisionForm #
	# fields = ['title','content','epigrafe','image']


######################### CONTACTO ##############################
class contactoView(ListView):
	model = Contacto
	template_name='blog/contacto.html'
	ordering = ['-id']


class editar_contacto(UpdateView):
	model = Contacto
	template_name = 'blog/editar_contacto.html'
	form_class = ContactoForm #
	# fields = ['title','content','epigrafe','image']



######################### REDES SOCIALES ##############################

class editar_redes(UpdateView):
	model = RedesSociales
	template_name = 'blog/editar_redes.html'
	form_class = RedesSocialesForm #
	# fields = ['title','content','epigrafe','image']

class redes(ListView):
	model = RedesSociales
	template_name='blog/redes.html'
	ordering = ['-id']

	