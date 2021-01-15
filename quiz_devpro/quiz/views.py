
from quiz_devpro.quiz.models import Pergunta
from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.

def indice(request):
    return render(request, 'quiz/indice.html')

def perguntas(request, indice):
    pergunta = Pergunta.objects.filter(disponivel=True).order_by('id')[indice -1]
    contexto = {'indice': indice, 'pergunta': pergunta}  
    return render(request, 'quiz/perguntas.html', contexto)

def classificacao(request):
    return render(request, 'quiz/classificacao.html')






