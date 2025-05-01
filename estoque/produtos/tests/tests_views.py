from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from produtos.models import Produto, Fornecedor, Categoria, Entrada, Saida

class ViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.fornecedor = Fornecedor.objects.create(nome='Fornecedor Teste', cnpj='12345678000195')
        self.categoria = Categoria.objects.create(nome='Categoria Teste', descricao='Teste de categoria')
        self.produto = Produto.objects.create(
            nome='Produto Teste', quantidade=10, preco=100.00, descricao='Teste', fornecedor=self.fornecedor, categoria=self.categoria
        )
        self.entrada = Entrada.objects.create(produto=self.produto, fornecedor=self.fornecedor, quantidade=5, valor_total=500.00)
        self.saida = Saida.objects.create(produto=self.produto, quantidade=3, valor_total=300.00)

    def test_listar_produtos(self):
        response = self.client.get(reverse('listar_produtos'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'listar_produtos.html')
        self.assertContains(response, 'Produto Teste')

    def test_adicionar_produto(self):
        response = self.client.post(reverse('adicionar_produto'), {
            'nome': 'Produto Novo', 'quantidade': 20, 'preco': 150.00, 'descricao': 'Descrição Nova',
            'fornecedor': self.fornecedor.id, 'categoria': self.categoria.id
        })
        self.assertRedirects(response, reverse('listar_produtos'))
        self.assertTrue(Produto.objects.filter(nome='Produto Novo').exists())

    def test_atualizar_produto(self):
        response = self.client.post(reverse('atualizar_produto', args=[self.produto.id]), {
            'nome': 'Produto Atualizado', 'quantidade': 15, 'preco': 120.00, 'descricao': 'Nova descrição',
            'fornecedor': self.fornecedor.id, 'categoria': self.categoria.id
        })
        self.produto.refresh_from_db()
        self.assertEqual(self.produto.nome, 'Produto Atualizado')
        self.assertEqual(self.produto.quantidade, 15)
        self.assertEqual(self.produto.preco, 120.00)
        self.assertRedirects(response, reverse('listar_produtos'))

    def test_detalhes_produto(self):
        response = self.client.get(reverse('detalhes_produto', args=[self.produto.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'detalhes_produto.html')

    def test_excluir_produto(self):
        response = self.client.post(reverse('excluir_produto', args=[self.produto.id]))
        self.assertRedirects(response, reverse('listar_produtos'))
        self.assertFalse(Produto.objects.filter(id=self.produto.id).exists())

    def test_custom_login(self):
        self.client.logout()
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'testpassword'})
        self.assertRedirects(response, reverse('listar_produtos'))

    def test_custom_logout(self):
        response = self.client.get(reverse('logout'))
        self.assertRedirects(response, reverse('login'))

    def test_registro_usuario(self):
        response = self.client.post(reverse('registro'), {
            'username': 'newuser', 'first_name': 'Novo', 'last_name': 'Usuário', 'email': 'novo@teste.com',
            'password1': 'teste12345', 'password2': 'teste12345'
        })
        self.assertRedirects(response, reverse('login'))
        self.assertTrue(User.objects.filter(username='newuser').exists())


class FornecedorViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.fornecedor = Fornecedor.objects.create(nome='Fornecedor Teste', cnpj='12345678901234')

    def test_listar_fornecedores(self):
        response = self.client.get(reverse('listar_fornecedores'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Fornecedor Teste')

    def test_adicionar_fornecedor(self):
        response = self.client.post(reverse('adicionar_fornecedor'), {'nome': 'Novo Fornecedor', 'cnpj': '98765432109876'})
        self.assertRedirects(response, reverse('listar_fornecedores'))
        self.assertTrue(Fornecedor.objects.filter(nome='Novo Fornecedor').exists())

    def test_atualizar_fornecedor(self):
        response = self.client.post(reverse('atualizar_fornecedor', args=[self.fornecedor.id]), {'nome': 'Fornecedor Atualizado', 'cnpj': '12345678901234'})
        self.assertRedirects(response, reverse('listar_fornecedores'))
        self.fornecedor.refresh_from_db()
        self.assertEqual(self.fornecedor.nome, 'Fornecedor Atualizado')

    def test_excluir_fornecedor(self):
        response = self.client.post(reverse('excluir_fornecedor', args=[self.fornecedor.id]))
        self.assertRedirects(response, reverse('listar_fornecedores'))
        self.assertFalse(Fornecedor.objects.filter(id=self.fornecedor.id).exists())


class CategoriaViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.categoria = Categoria.objects.create(nome='Categoria Teste')

    def test_listar_categorias(self):
        response = self.client.get(reverse('listar_categorias'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Categoria Teste')

    def test_adicionar_categoria(self):
        response = self.client.post(reverse('adicionar_categoria'), {'nome': 'Nova Categoria'})
        self.assertRedirects(response, reverse('listar_categorias'))
        self.assertTrue(Categoria.objects.filter(nome='Nova Categoria').exists())

    def test_atualizar_categoria(self):
        response = self.client.post(reverse('atualizar_categoria', args=[self.categoria.id]), {'nome': 'Categoria Atualizada'})
        self.assertRedirects(response, reverse('listar_categorias'))
        self.categoria.refresh_from_db()
        self.assertEqual(self.categoria.nome, 'Categoria Atualizada')

    def test_excluir_categoria(self):
        response = self.client.post(reverse('excluir_categoria', args=[self.categoria.id]))
        self.assertRedirects(response, reverse('listar_categorias'))
        self.assertFalse(Categoria.objects.filter(id=self.categoria.id).exists())


class EntradaViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.categoria = Categoria.objects.create(nome='Categoria Teste')
        self.produto = Produto.objects.create(nome='Produto Teste', quantidade=10, preco=100, categoria=self.categoria)
        self.fornecedor = Fornecedor.objects.create(nome='Fornecedor Teste', cnpj='12345678901234')
        self.entrada = Entrada.objects.create(produto=self.produto, fornecedor=self.fornecedor, quantidade=5, valor_total=500)

    def test_listar_entradas(self):
        response = self.client.get(reverse('listar_entradas'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Produto Teste')

    def test_adicionar_entrada(self):
        response = self.client.post(reverse('adicionar_entrada'), {'produto': self.produto.id, 'fornecedor': self.fornecedor.id, 'quantidade': 3, 'valor_total': 300})
        self.assertRedirects(response, reverse('listar_entradas'))
        self.assertTrue(Entrada.objects.filter(quantidade=3).exists())

    def test_excluir_entrada(self):
        response = self.client.post(reverse('excluir_entrada', args=[self.entrada.id]))
        self.assertRedirects(response, reverse('listar_entradas'))
        self.assertFalse(Entrada.objects.filter(id=self.entrada.id).exists())


class SaidaViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.categoria = Categoria.objects.create(nome='Categoria Teste')
        self.produto = Produto.objects.create(nome='Produto Teste', quantidade=10, preco=100, categoria=self.categoria)
        self.saida = Saida.objects.create(produto=self.produto, quantidade=2, valor_total=200)

    def test_listar_saidas(self):
        response = self.client.get(reverse('listar_saidas'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Produto Teste')

    def test_adicionar_saida(self):
        response = self.client.post(reverse('adicionar_saida'), {'produto': self.produto.id, 'quantidade': 1, 'valor_total': 100})
        self.assertRedirects(response, reverse('listar_saidas'))
        self.assertTrue(Saida.objects.filter(quantidade=1).exists())

    def test_excluir_saida(self):
        response = self.client.post(reverse('excluir_saida', args=[self.saida.id]))
        self.assertRedirects(response, reverse('listar_saidas'))
        self.assertFalse(Saida.objects.filter(id=self.saida.id).exists())
