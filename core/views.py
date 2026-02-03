from urllib import request
from django.shortcuts import render, redirect

from django.http import HttpResponse

def home(request):
    return render(request, "core/home.html") 

chamados = [

    {'id' : 1, 'Setor': 'TI', 'problema': 'Computador lento', 'prioridade': 'Alta', 'descricao': 'O computador está muito lento ao iniciar.'},
    {'id' : 2, 'Setor': 'RH', 'problema': 'Erro no sistema de folha de pagamento', 'prioridade': 'Média', 'descricao': 'O sistema não está calculando os impostos corretamente.'},
    {'id' : 3, 'Setor': 'Financeiro', 'problema': 'Falta de acesso ao sistema bancário', 'prioridade': 'Alta', 'descricao': 'Não consigo acessar o sistema bancário para realizar pagamentos.'},
]
def listar (request):
  
   return render(request, "core/listar.html", {"chamados": chamados})

def criar (request):

    return render(request, "core/criar.html")

def fechar (request, id):
    if 0 <= id < len(chamados):
        chamados.pop(id)
      
    return render(request, "core/fechar.html", {"message": "O chamado foi fechado com sucesso!"})
    
def Exibirfechar (request, id):
    if 0 <= id < len(chamados):
        chamados.pop(id)
    return render(request, "core/fechar.html", {"message": "O chamado foi fechado com sucesso!"})
    

def novoChamado(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        Setor = request.POST.get('Setor')
        problema = request.POST.get('problema')
        prioridade = request.POST.get('prioridade')
        descricao = request.POST.get('descricao')
        
        print("Chegou um POST")
        print(f"Setor: {Setor}, problema: {problema}, prioridade: {prioridade}, descricao: {descricao}")
        chamados.append({
             "Setor": Setor,
             "problema": problema,
             "prioridade": prioridade, # ou "Media"
             "descricao": descricao })
        
        return redirect('listar')
     
    if request.method == "GET":
        print("Chegou um GET")
        return render(request, 'core/novochamado.html')
        
       
# Create your views here.
