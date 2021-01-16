from quiz_devpro.quiz.models import Alunos, Pergunta
from django.contrib import admin

# Register your models here.


@admin.register(Pergunta)
class PerguntaAdmin(admin.ModelAdmin):
    list_display = ['id', 'enunciado', 'disponivel']

@admin.register(Alunos)
class AlunosAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'email', 'criacao']
