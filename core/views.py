from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Hello World!</h1><p>Meu primeiro sistema Django está online.</p>")

chamados = [

    {'Setor': 'TI', 'problema': 'Computador lento', 'prioridade': 'Alta', 'descricao': 'O computador está muito lento ao iniciar.'},
    {'Setor': 'RH', 'problema': 'Erro no sistema de folha de pagamento', 'prioridade': 'Média', 'descricao': 'O sistema não está calculando os impostos corretamente.'},
    {'Setor': 'Financeiro', 'problema': 'Falta de acesso ao sistema bancário', 'prioridade': 'Alta', 'descricao': 'Não consigo acessar o sistema bancário para realizar pagamentos.'},
]
def listar (request):
   html = "<h1>Listar Chamados</h1><ul>"
   for chamado in chamados:
       html += f"<li><strong>Setor: {chamado['Setor']} - Problema: {chamado['problema']} - Prioridade: {chamado['prioridade']} - Descrição: {chamado['descricao']}</li>"
   html += "</ul>"
   return HttpResponse(html)

def criar (request, Setor, problema, prioridade, descricao):


    novo =  { 
    'Setor': Setor,
    'problema': problema,
    'prioridade': prioridade,
    'descricao': descricao
}
    chamados.append(novo)
    return HttpResponse(f"<h1>Novo chamado criado com sucesso!</h1><p>Setor: {Setor}</p><p>Problema: {problema}</p><p>Prioridade: {prioridade}</p><p>Descrição: {descricao}</p>")




# Create your views here.
