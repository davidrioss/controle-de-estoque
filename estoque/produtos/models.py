from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, MinValueValidator

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=500, blank=True)
    
    def __str__(self):
        return self.nome
    

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    quantidade = models.IntegerField(validators=[MinValueValidator(0)]) #quantidade minima 0
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.CharField(max_length=500, blank=True)
    fornecedor = models.ForeignKey('Fornecedor', on_delete=models.CASCADE)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome
    
    
def validar_cnpj(value):
    if not value.isdigit() or len(value) != 14:
        raise ValidationError("CNPJ deve conter 14 dígitos numéricos.")


class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14, unique=True, validators=[validar_cnpj])
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    endereco = models.CharField(max_length=200)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    cep = models.CharField(max_length=8)
    
    def __str__(self): 
        return self.nome
    
    
class Entrada(models.Model):
    produto = models.ForeignKey('Produto', on_delete=models.CASCADE)
    fornecedor = models.ForeignKey('Fornecedor', on_delete=models.CASCADE)
    quantidade = models.IntegerField(validators=[MinValueValidator(1)]) #quantidade minima 1
    data = models.DateField(auto_now_add=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.produto} - {self.data}"
    
    def save(self, *args, **kwargs):
        # Atualiza o estoque do produto ao salvar uma entrada
        if not self.pk:  # Verifica se é uma nova entrada
            self.produto.quantidade += self.quantidade
            self.produto.save()
        super().save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        self.produto.quantidade -= self.quantidade
        self.produto.save()
        super().delete(*args, **kwargs)


class Saida(models.Model):
    produto = models.ForeignKey('Produto', on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    data = models.DateField(auto_now_add=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)

    #validação para ver se o estoque é sulficiente para a retirada desejada
    def clean(self):
        if not self.produto:
            raise ValidationError("O campo 'produto' não pode estar vazio.")
        if self.quantidade > self.produto.quantidade:
            raise ValidationError("A quantidade retirada não pode exceder o estoque disponível.")

    def __str__(self):
        return f"{self.produto} - {self.data}"
    
    def save(self, *args, **kwargs):
        # Atualiza o estoque do produto ao salvar uma saída
        if not self.pk:  # Verifica se é uma nova saída
            self.produto.quantidade -= self.quantidade
            self.produto.save()
        super().save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        self.produto.quantidade += self.quantidade if isinstance(self, Saida) else -self.quantidade
        self.produto.save()
        super().delete(*args, **kwargs)
 


"""
Comandos SQL
-----------------------------------------------Inserção de Dados------------------------------------

Categoria:
    INSERT INTO produtos_categoria (nome, descricao) VALUES ('Eletrônicos', 'Aparelhos eletrônicos e acessórios');
    INSERT INTO produtos_categoria (nome, descricao) VALUES ('Móveis', 'Móveis para casa e escritório');

Fornecedor:
    INSERT INTO produtos_fornecedor (nome, cnpj, email, telefone, endereco, cidade, estado, cep) 
    VALUES ('Fornecedor A', '12345678000199', 'contato@fornecedora.com', '11999999999', 'Rua A, 100', 'São Paulo', 'SP', '01001000');

    INSERT INTO produtos_fornecedor (nome, cnpj, email, telefone, endereco, cidade, estado, cep) 
    VALUES ('Fornecedor B', '98765432000100', 'contato@fornecedorb.com', '21988888888', 'Rua B, 200', 'Rio de Janeiro', 'RJ', '22020010');

Produto:
    INSERT INTO produtos_produto (nome, quantidade, preco, descricao, fornecedor_id, categoria_id) 
    VALUES ('Smartphone', 50, 1500.00, 'Celular de última geração', 1, 1);

    INSERT INTO produtos_produto (nome, quantidade, preco, descricao, fornecedor_id, categoria_id) 
    VALUES ('Mesa de Escritório', 30, 500.00, 'Mesa com 4 gavetas', 2, 2);

Entrada:
    INSERT INTO produtos_entrada (produto_id, fornecedor_id, quantidade, valor_total, data) 
    VALUES (1, 1, 10, 15000.00, DATE('now'));

    INSERT INTO produtos_entrada (produto_id, fornecedor_id, quantidade, valor_total, data) 
    VALUES (2, 2, 5, 2500.00, DATE('now'));

Saida:
    INSERT INTO produtos_saida (produto_id, quantidade, valor_total, data) 
    VALUES (1, 5, 7500.00, DATE('now'));

    INSERT INTO produtos_saida (produto_id, quantidade, valor_total, data) 
    VALUES (2, 2, 1000.00, DATE('now'));

-------------------------------------Consultas-------------------------------------------------

Consultar todas as categorias:
    SELECT * FROM produtos_categoria;

Consultar todos os fornecedores:
    SELECT * FROM produtos_fornecedor;

Consultar todos os produtos com detalhes de fornecedor e categoria:
    SELECT p.id, p.nome AS produto, p.quantidade, p.preco, f.nome AS fornecedor, c.nome AS categoria
    FROM produtos_produto p
    JOIN produtos_fornecedor f ON p.fornecedor_id = f.id
    JOIN produtos_categoria c ON p.categoria_id = c.id;

Consultar entradas realizadas com detalhes do produto e fornecedor:
    SELECT e.id, p.nome AS produto, f.nome AS fornecedor, e.quantidade, e.valor_total, e.data
    FROM produtos_entrada e
    JOIN produtos_produto p ON e.produto_id = p.id
    JOIN produtos_fornecedor f ON e.fornecedor_id = f.id;

Consultar saídas realizadas com detalhes do produto:
    SELECT s.id, p.nome AS produto, s.quantidade, s.valor_total, s.data
    FROM produtos_saida s
    JOIN produtos_produto p ON s.produto_id = p.id;

Verificar estoque atual dos produtos:
    SELECT p.id, p.nome AS produto, p.quantidade AS estoque_atual
    FROM produtos_produto p;

Produtos com quantidade abaixo de um limite (por exemplo, 10 unidades):
    SELECT id, nome, quantidade 
    FROM produtos_produto 
    WHERE quantidade < 10;

Fornecedores que fornecem produtos na categoria "Eletrônicos":
    SELECT DISTINCT f.id, f.nome AS fornecedor
    FROM produtos_fornecedor f
    JOIN produtos_produto p ON f.id = p.fornecedor_id
    JOIN produtos_categoria c ON p.categoria_id = c.id
    WHERE c.nome = 'Eletrônicos';

            
        
"""