from django.test import TestCase
from produtos.forms import ProdutoForm, FornecedorForm, CategoriaForm, EntradaForm, SaidaForm, RegistroUsuarioForm
from produtos.models import Produto, Fornecedor, Categoria, Entrada, Saida
from django.contrib.auth.models import User

class ProdutoFormTest(TestCase):
    def test_produto_form_valid(self):
        categoria = Categoria.objects.create(nome="Eletrônicos", descricao="Aparelhos eletrônicos")
        fornecedor = Fornecedor.objects.create(nome="Fornecedor A", cnpj="12345678000199", email="email@email.com", telefone="11999999999", endereco="Rua A, 100", cidade="São Paulo", estado="SP", cep="01001000")
        form = ProdutoForm(data={
            'nome': 'Smartphone',
            'quantidade': 10,
            'preco': 1500.00,
            'descricao': 'Celular novo',
            'fornecedor': fornecedor.id,
            'categoria': categoria.id
        })
        self.assertTrue(form.is_valid())

    def test_produto_form_invalid(self):
        form = ProdutoForm(data={})  # Formulário vazio
        self.assertFalse(form.is_valid())
        self.assertIn('nome', form.errors)


class FornecedorFormTest(TestCase):
    def test_fornecedor_form_valid(self):
        form = FornecedorForm(data={
            'nome': 'Fornecedor B',
            'cnpj': '98765432000100',
            'email': 'fornecedor@email.com',
            'telefone': '11999999999',
            'endereco': 'Rua B, 200',
            'cidade': 'Rio de Janeiro',
            'estado': 'RJ',
            'cep': '22020010'
        })
        self.assertTrue(form.is_valid())

    def test_fornecedor_form_invalid_cnpj(self):
        form = FornecedorForm(data={
            'nome': 'Fornecedor C',
            'cnpj': '123',  # CNPJ inválido
            'email': 'fornecedor@email.com',
            'telefone': '11999999999',
            'endereco': 'Rua C, 300',
            'cidade': 'Belo Horizonte',
            'estado': 'MG',
            'cep': '30110000'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('cnpj', form.errors)


class CategoriaFormTest(TestCase):
    def test_categoria_form_valid(self):
        form = CategoriaForm(data={
            'nome': 'Móveis',
            'descricao': 'Móveis para casa e escritório'
        })
        self.assertTrue(form.is_valid())

    def test_categoria_form_invalid(self):
        form = CategoriaForm(data={})  # Formulário vazio
        self.assertFalse(form.is_valid())
        self.assertIn('nome', form.errors)


class EntradaFormTest(TestCase):
    def test_entrada_form_valid(self):
        categoria = Categoria.objects.create(nome="Eletrônicos", descricao="Aparelhos eletrônicos")
        fornecedor = Fornecedor.objects.create(nome="Fornecedor A", cnpj="12345678000199", email="email@email.com", telefone="11999999999", endereco="Rua A, 100", cidade="São Paulo", estado="SP", cep="01001000")
        produto = Produto.objects.create(nome='Smartphone', quantidade=10, preco=1500.00, descricao='Celular novo', fornecedor=fornecedor, categoria=categoria)
        form = EntradaForm(data={
            'produto': produto.id,
            'fornecedor': fornecedor.id,
            'quantidade': 5,
            'valor_total': 7500.00
        })
        self.assertTrue(form.is_valid())

    def test_entrada_form_invalid(self):
        form = EntradaForm(data={})  # Formulário vazio
        self.assertFalse(form.is_valid())
        self.assertIn('produto', form.errors)


class SaidaFormTest(TestCase):
    def test_saida_form_valid(self):
        categoria = Categoria.objects.create(nome="Eletrônicos", descricao="Aparelhos eletrônicos")
        fornecedor = Fornecedor.objects.create(nome="Fornecedor A", cnpj="12345678000199", email="email@email.com", telefone="11999999999", endereco="Rua A, 100", cidade="São Paulo", estado="SP", cep="01001000")
        produto = Produto.objects.create(nome='Smartphone', quantidade=10, preco=1500.00, descricao='Celular novo', fornecedor=fornecedor, categoria=categoria)
        form = SaidaForm(data={
            'produto': produto.id,
            'quantidade': 5,
            'valor_total': 7500.00
        })
        self.assertTrue(form.is_valid())

    def test_saida_form_invalid(self):
        form = SaidaForm(data={'quantidade': 15})  # Sem produto
        self.assertFalse(form.is_valid())
        self.assertIn('produto', form.errors)


class RegistroUsuarioFormTest(TestCase):
    def test_registro_usuario_form_valid(self):
        form = RegistroUsuarioForm(data={
            'username': 'usuario_teste',
            'first_name': 'Usuário',
            'last_name': 'Teste',
            'email': 'usuario@email.com',
            'password1': 'SenhaForte123',
            'password2': 'SenhaForte123'
        })
        self.assertTrue(form.is_valid())

    def test_registro_usuario_form_invalid_password_mismatch(self):
        form = RegistroUsuarioForm(data={
            'username': 'usuario_teste',
            'first_name': 'Usuário',
            'last_name': 'Teste',
            'email': 'usuario@email.com',
            'password1': 'SenhaForte123',
            'password2': 'SenhaDiferente'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors)

    def test_registro_usuario_form_invalid_missing_fields(self):
        form = RegistroUsuarioForm(data={})  # Formulário vazio
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)
        self.assertIn('password1', form.errors)
