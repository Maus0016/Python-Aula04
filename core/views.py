from django.http import HttpResponse
from django.shortcuts import render, redirect


chamados = [
#Banco de dados em memoria
    {"id": 1, 'Setor': 'TI', 'problema': 'Computador lento', 'prioridade': 'Alta', 'descricao': 'O computador está muito lento ao iniciar.'},
    {"id": 2, 'Setor': 'RH', 'problema': 'Erro no sistema de folha de pagamento', 'prioridade': 'Média', 'descricao': 'O sistema não está calculando os impostos corretamente.'},
    {"id": 3,  'Setor': 'Financeiro', 'problema': 'Falta de acesso ao sistema bancário', 'prioridade': 'Alta', 'descricao': 'Não consigo acessar o sistema bancário para realizar pagamentos.'},
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
        return redirect('./listar_chamados')


    return render(request, "core/novoChamado.html")

def fechar(request, id):
    for chamado in chamados:
        if chamado["id"] == id:
            chamados.remove(chamado)
            break

    return redirect('/listar_chamados')

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
    return render(request, 'core/novaCategoria.html')

def editar_categoria(request, id):
    categoria = categorias.objects.get(id=id)
    if request.method == "POST":
        categorias.nome = request.POST.get('nome')
        categorias.save
        return redirect('/listar_categorias')

    if request.method == "GET":
     return render(request, 'core/editar_categoria.html', {'categorias' : categorias} )


def excluir_categoria(request, id):
    for categoria in categorias:
        if categoria["id"] == id:
            categorias.remove(categoria)
            break
    return redirect('/listar_categorias')

