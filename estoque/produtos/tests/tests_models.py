from django.test import TestCase
from django.core.exceptions import ValidationError
from produtos.models import Categoria, Produto, Fornecedor, Entrada, Saida

class CategoriaModelTest(TestCase):
    def test_criar_categoria(self):
        categoria = Categoria.objects.create(nome="Eletrônicos", descricao="Itens eletrônicos")
        self.assertEqual(categoria.nome, "Eletrônicos")

    def test_categoria_nome_vazio(self):
        categoria = Categoria(nome="")
        with self.assertRaises(ValidationError):
            categoria.full_clean()

class FornecedorModelTest(TestCase):
    def test_criar_fornecedor(self):
        fornecedor = Fornecedor.objects.create(
            nome="Fornecedor A",
            cnpj="12345678000199",
            email="fornecedor@email.com",
            telefone="11999999999",
            endereco="Rua A, 100",
            cidade="São Paulo",
            estado="SP",
            cep="01001000"
        )
        self.assertEqual(fornecedor.nome, "Fornecedor A")
    
    def test_cnpj_invalido(self):
        fornecedor = Fornecedor(nome="Fornecedor Inválido", cnpj="1234")
        with self.assertRaises(ValidationError):
            fornecedor.full_clean()

class ProdutoModelTest(TestCase):
    def setUp(self):
        self.categoria = Categoria.objects.create(nome="Eletrônicos")
        self.fornecedor = Fornecedor.objects.create(
            nome="Fornecedor A",
            cnpj="12345678000199",
            email="fornecedor@email.com",
            telefone="11999999999",
            endereco="Rua A, 100",
            cidade="São Paulo",
            estado="SP",
            cep="01001000"
        )
    
    def test_criar_produto(self):
        produto = Produto.objects.create(
            nome="Smartphone",
            quantidade=10,
            preco=1500.00,
            descricao="Celular de última geração",
            fornecedor=self.fornecedor,
            categoria=self.categoria
        )
        self.assertEqual(produto.nome, "Smartphone")
    
    def test_quantidade_negativa(self):
        produto = Produto(
            nome="TV",
            quantidade=-5,
            preco=2000.00,
            fornecedor=self.fornecedor,
            categoria=self.categoria
        )
        with self.assertRaises(ValidationError):
            produto.full_clean()

class EntradaModelTest(TestCase):
    def setUp(self):
        self.categoria = Categoria.objects.create(nome="Eletrônicos")
        self.fornecedor = Fornecedor.objects.create(
            nome="Fornecedor A",
            cnpj="12345678000199",
            email="fornecedor@email.com",
            telefone="11999999999",
            endereco="Rua A, 100",
            cidade="São Paulo",
            estado="SP",
            cep="01001000"
        )
        self.produto = Produto.objects.create(
            nome="Smartphone",
            quantidade=10,
            preco=1500.00,
            fornecedor=self.fornecedor,
            categoria=self.categoria
        )
    
    def test_entrada_aumenta_estoque(self):
        entrada = Entrada.objects.create(
            produto=self.produto,
            fornecedor=self.fornecedor,
            quantidade=5,
            valor_total=7500.00
        )
        self.produto.refresh_from_db()
        self.assertEqual(self.produto.quantidade, 15)
    
class SaidaModelTest(TestCase):
    def setUp(self):
        self.categoria = Categoria.objects.create(nome="Eletrônicos")
        self.fornecedor = Fornecedor.objects.create(
            nome="Fornecedor A",
            cnpj="12345678000199",
            email="fornecedor@email.com",
            telefone="11999999999",
            endereco="Rua A, 100",
            cidade="São Paulo",
            estado="SP",
            cep="01001000"
        )
        self.produto = Produto.objects.create(
            nome="Smartphone",
            quantidade=10,
            preco=1500.00,
            fornecedor=self.fornecedor,
            categoria=self.categoria
        )
    
    def test_saida_diminui_estoque(self):
        saida = Saida.objects.create(
            produto=self.produto,
            quantidade=3,
            valor_total=4500.00
        )
        self.produto.refresh_from_db()
        self.assertEqual(self.produto.quantidade, 7)
    
    def test_saida_maior_que_estoque(self):
        saida = Saida(produto=self.produto, quantidade=15, valor_total=22500.00)
        with self.assertRaises(ValidationError):
            saida.full_clean()
