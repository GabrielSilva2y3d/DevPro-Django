from quiz_devpro.quiz.models import Pergunta
from django.contrib import admin

# Register your models here.


@admin.register(Pergunta)
class PerguntaAdmin(admin.ModelAdmin):
    list_display = ['id', 'enunciado', 'disponivel']