from django.shortcuts import render
from django.http import HttpResponse
from .models import Perfil
# Create your views here.

def index(request):
	import random
	n = random.randint(0,100)
	return render(request, 'index.html', 
		          {'nome':'ely', 'n' : n})

def exibir_perfil(request, perfil_id):

	perfil = get(perfil_id)
	return render(request, 'perfil.html', 
		          {'perfil' : perfil})


def get(perfil_id):
	if (perfil_id == 1):
		return Perfil('Ely', 'ely@ifpi.edu.br',
						'99999-9999', 'ifpi')				
	if (perfil_id == 2):
		return Perfil('Pedro', 'pedro@gmail.com',
						'99999-8888', 'Google')				
	if (perfil_id == 3):
		return Perfil('Maria', 'maria@hotmail.com',
						'88888-7777', 'MS')				
