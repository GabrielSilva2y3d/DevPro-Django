
from quiz_devpro.quiz.form import AlunoForm
from quiz_devpro.quiz.models import Alunos, Pergunta
from django.http.response import HttpResponse
from django.shortcuts import redirect, render

# Create your views here.

def indice(request):
    if request.method == 'POST':
        #verificar se ja existe um usuário com o email enviado
        email = request.POST['email']
        try:
            aluno = Alunos.objects.get(email=email)
        except Alunos.DoesNotExist:
            #Validar o formulario
            form = AlunoForm(request.POST)
            if form.is_valid():
             #salvar no banco de dados e redirecionar o usuário para o quiz
             aluno = form.save()
             request.session['aluno_id'] = aluno.id  
             return redirect('/perguntas/1')
            #Se não for valido apresentar formulario com erros
            contexto = {'form': form}
            return render(request, 'quiz/indice.html', contexto)
        else:
            request.session['aluno_id'] = aluno.id 
            return redirect('/perguntas/1')

        

    return render(request, 'quiz/indice.html')

def perguntas(request, indice):
    aluno_id = request.session['aluno_id']
    try:
        pergunta = Pergunta.objects.filter(disponivel=True).order_by('id')[indice - 1]
    except IndexError:
        return redirect('/classificacao')
    else:
        contexto = {'indice': indice, 'pergunta': pergunta}  

        if request.method == 'POST':
            alter_escolhida = int(request.POST['alternativa'])
            
            if alter_escolhida == pergunta.alter_correta:
                #guardar resposta e calcular pontos
                return redirect(f'/perguntas/{indice + 1}')
            contexto['alter_escolhida'] = alter_escolhida
        
        return render(request, 'quiz/perguntas.html', contexto)

def classificacao(request):
    return render(request, 'quiz/classificacao.html')






