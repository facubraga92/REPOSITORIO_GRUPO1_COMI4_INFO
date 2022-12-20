from django.shortcuts import render , redirect

# Create your views here.

def inicio(request):
	

	return render(request, 'blog/index.html');



def login(request):
	return render(request,'blog/login.html');


def contacto(request):
	return render(request,'blog/contacto.html');


	
def quienessomos(request):
	return render(request,'blog/quienessomos.html');