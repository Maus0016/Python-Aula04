from django.db import models
 
class Chamado(models.Model):
    # Texto curto (max 100 letras)
    Setor = models.CharField(max_length=100)
    
    # Texto longo (sem limite de letras)
    descricao = models.TextField()
    
    # Escolhas pré-definidas
    OPCOES_PRIORIDADE = [
        ('Baixa', 'Baixa'),
        ('Média', 'Média'),
        ('Alta', 'Alta'),
    ]
    prioridade = models.CharField(max_length=10, choices=OPCOES_PRIORIDADE, default='Média')
    
    # Data e Hora automática no momento da criação
    data_criacao = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"{self.Setor} - {self.prioridade}"
    

    
class Categoria(models.Model):
    # Texto curto (max 100 letras)
    nome = models.CharField(max_length=100)
    
    # Data e Hora automática no momento da criação
    data_criacao = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"{self.nome}"
    
    class Equipamento(models.Model):
        descricao = models.CharField(max_length=250)
        tipo = models.CharField(max_length=50)
        ocupado =models.BooleanField()

        OPCOES_CONDICAO = [
            ('Novo', 'Novo'),
            ('Usado', 'Usado'),
            ('Defeituiso', 'Defeituoso'),

        ] 
        condicao = models.CharField(max_length=50, choices=OPCOES_CONDICAO, default='Novo')

        data_criacao = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"{self.descricao} - {self.tipo}"
    
    class Pessoa(models.Model):
        cpf = models.IntegerField()
        rg = models.IntegerField()
        nome = models.CharField(max_length=15)
        sobrenome = models.CharField(max_length=15)
        idade = models.IntegerField()
        telefone = models.IntegerField()
        email = models.EmailField()
        dt_nascimento = models.DateField()
        cep = models.IntegerField()
        endereco = models.CharField(max_length=20)
        complemento = models.TextField(max_length=60)
        status = models.BooleanField() # Online/Off

        data_criacao = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"{self.descricao} - {self.tipo}"