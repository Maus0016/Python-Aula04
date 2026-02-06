from django.http import HttpResponse
from django.shortcuts import render, redirect


chamados = [
#Banco de dados em memoria
    {'Setor': 'TI', 'problema': 'Computador lento', 'prioridade': 'Alta', 'descricao': 'O computador está muito lento ao iniciar.'},
    {'Setor': 'RH', 'problema': 'Erro no sistema de folha de pagamento', 'prioridade': 'Média', 'descricao': 'O sistema não está calculando os impostos corretamente.'},
    {'Setor': 'Financeiro', 'problema': 'Falta de acesso ao sistema bancário', 'prioridade': 'Alta', 'descricao': 'Não consigo acessar o sistema bancário para realizar pagamentos.'},
]

categorias = [
        {"id": 1, "nome": "Chamado teste"},
        {"id": 2, "nome": "Sem acesso a internet"},
        {"id": 3, "nome": "Configurar mouse"},
]

def home(request):
    return render(request, "core/home.html") 

def novoChamado(request):
    #Enviar dados POST
    if request.method == "POST":
    #Capturando os dados
        Setor = request.POST.get('Setor')
        problema = request.POST.get('problema')
        prioridade = request.POST.get('prioridade')
        descricao = request.POST.get('descricao')
    #Salva a base de dados
        print(f"Recebido: {Setor}, {problema}, {prioridade}, {descricao}")

        chamados.append({
            "id": len(chamados) + 1,
            "Setor": Setor,
            "problema": problema,
            "prioridade": prioridade,
            "descricao": descricao
        })

    #Redireciona de volta para a lista
        return redirect('./listar')


    return render(request, "core/novoChamado.html")

def fechar(request, id):
    for chamado in chamados:
        if chamado["id"] == id:
            chamados.remove(chamado)
            break

    return redirect('/listar')

def listarChamados(request):
    return render(request, 'core/listar.html', {"chamados": chamados})      

def listar_categorias(request):
    return render(request, 'core/listar_categorias.html', {"categorias": categorias})

def nova_categoria(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        categorias.append({
            "id": len(categorias) + 1,
            "nome": nome
        })
        # salvar meus dados
        return redirect('/listar_categorias')
    return render(request, 'core/nova_categoria.html')

def excluir_categoria(request, id):
    for categoria in categorias:
        if categoria["id"] == id:
            categorias.remove(categoria)
            break
    return redirect('/listar_categorias')



























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
