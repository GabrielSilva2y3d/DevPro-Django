from quiz_devpro.quiz.models import Alunos
from django.forms import ModelForm

class AlunoForm(ModelForm):
    class Meta:
        model = Alunos
        fields = ['nome', 'email']
