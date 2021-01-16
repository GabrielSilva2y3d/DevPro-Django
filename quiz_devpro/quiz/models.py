from django.db import models

# Create your models here.

class Pergunta(models.Model):
    enunciado = models.TextField()
    alternativas = models.JSONField()
    disponivel = models.BooleanField(default=False)
    alter_correta = models.IntegerField(choices=[
        (0, 'A'),
        (1, 'B'),
        (2, 'C'),
        (3, 'D'), 
    ])

class Alunos(models.Model):
    nome = models.CharField(max_length=64)
    email = models.EmailField(unique=True)
    criacao = models.DateField(auto_now_add=True)
    