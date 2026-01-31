from urllib import request
from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return render(request, "core/home.html") 

chamados = [

    {'Setor': 'TI', 'problema': 'Computador lento', 'prioridade': 'Alta', 'descricao': 'O computador está muito lento ao iniciar.'},
    {'Setor': 'RH', 'problema': 'Erro no sistema de folha de pagamento', 'prioridade': 'Média', 'descricao': 'O sistema não está calculando os impostos corretamente.'},
    {'Setor': 'Financeiro', 'problema': 'Falta de acesso ao sistema bancário', 'prioridade': 'Alta', 'descricao': 'Não consigo acessar o sistema bancário para realizar pagamentos.'},
]
def listar (request):
  
   return render(request, "core/listar.html", {"chamados": chamados})

def criar (request, Setor, problema, prioridade, descricao):


    novo =  { 
    'Setor': Setor,
    'problema': problema,
    'prioridade': prioridade,
    'descricao': descricao
}
    chamados.append(novo)
    return render(request, "core/criar.html", {"Setor": Setor, "problema": problema, "prioridade": prioridade, "descricao": descricao})

def fechar (request, indice):
    if 0 <= indice < len(chamados):
        chamados.pop(indice)
        request.method == 'POST'
        request.method == 'GET'
        request.method == 'DELETE'
    return render(request, "core/fechar.html", {"message": "O chamado foi fechado com sucesso!"})
    
    

def novoChamado (request):
    if request.method == 'GET':
        return render(request, "core/novoChamado.html")
    

    if request.method == 'POST':
        Setor = request.POST.get('Setor')
        problema = request.POST.get('problema')
        prioridade = request.POST.get('prioridade')
        descricao = request.POST.get('descricao')

        print ("Chegou um post")
        print ("Setor: {Setor}, problema: {problema}, prioridade: {prioridade}, descricao: {descricao}")

        chamados.append(
            "Setor: " Setor,
            "problema: " problema,
            "prioridade: " prioridade,
            "descricao: " descricao
        )
        

        return render(request, "core/criar.html", {"Setor": Setor, "problema": problema, "prioridade": prioridade, "descricao": descricao})

  
    return render(request, "core/novoChamado.html")

# Create your views here.
