from django.test import SimpleTestCase
from django.urls import reverse, resolve
from produtos.views import *

class TestUrls(SimpleTestCase):
    
    def test_login_url_resolves(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func, custom_login)
    
    def test_logout_url_resolves(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func, custom_logout)
    
    def test_perfil_url_resolves(self):
        url = reverse('perfil_usuario')
        self.assertEqual(resolve(url).func, perfil_usuario)
    
    def test_registro_url_resolves(self):
        url = reverse('registro')
        self.assertEqual(resolve(url).func, registro)
    
    def test_listar_produtos_url_resolves(self):
        url = reverse('listar_produtos')
        self.assertEqual(resolve(url).func, listar_produtos)
    
    def test_adicionar_produto_url_resolves(self):
        url = reverse('adicionar_produto')
        self.assertEqual(resolve(url).func, adicionar_produto)
    
    def test_atualizar_produto_url_resolves(self):
        url = reverse('atualizar_produto', args=[1])
        self.assertEqual(resolve(url).func, atualizar_produto)
    
    def test_detalhes_produto_url_resolves(self):
        url = reverse('detalhes_produto', args=[1])
        self.assertEqual(resolve(url).func, detalhes_produto)
    
    def test_excluir_produto_url_resolves(self):
        url = reverse('excluir_produto', args=[1])
        self.assertEqual(resolve(url).func, excluir_produto)
    
    def test_listar_fornecedores_url_resolves(self):
        url = reverse('listar_fornecedores')
        self.assertEqual(resolve(url).func, listar_fornecedores)
    
    def test_adicionar_fornecedor_url_resolves(self):
        url = reverse('adicionar_fornecedor')
        self.assertEqual(resolve(url).func, adicionar_fornecedor)
    
    def test_atualizar_fornecedor_url_resolves(self):
        url = reverse('atualizar_fornecedor', args=[1])
        self.assertEqual(resolve(url).func, atualizar_fornecedor)
    
    def test_detalhes_fornecedor_url_resolves(self):
        url = reverse('detalhes_fornecedor', args=[1])
        self.assertEqual(resolve(url).func, detalhes_fornecedor)
    
    def test_excluir_fornecedor_url_resolves(self):
        url = reverse('excluir_fornecedor', args=[1])
        self.assertEqual(resolve(url).func, excluir_fornecedor)
    
    def test_listar_categorias_url_resolves(self):
        url = reverse('listar_categorias')
        self.assertEqual(resolve(url).func, listar_categorias)
    
    def test_adicionar_categoria_url_resolves(self):
        url = reverse('adicionar_categoria')
        self.assertEqual(resolve(url).func, adicionar_categoria)
    
    def test_atualizar_categoria_url_resolves(self):
        url = reverse('atualizar_categoria', args=[1])
        self.assertEqual(resolve(url).func, atualizar_categoria)
    
    def test_detalhes_categoria_url_resolves(self):
        url = reverse('detalhes_categoria', args=[1])
        self.assertEqual(resolve(url).func, detalhes_categoria)
    
    def test_excluir_categoria_url_resolves(self):
        url = reverse('excluir_categoria', args=[1])
        self.assertEqual(resolve(url).func, excluir_categoria)
    
    def test_listar_entradas_url_resolves(self):
        url = reverse('listar_entradas')
        self.assertEqual(resolve(url).func, listar_entradas)
    
    def test_adicionar_entrada_url_resolves(self):
        url = reverse('adicionar_entrada')
        self.assertEqual(resolve(url).func, adicionar_entrada)
    
    def test_atualizar_entrada_url_resolves(self):
        url = reverse('atualizar_entrada', args=[1])
        self.assertEqual(resolve(url).func, atualizar_entrada)
    
    def test_detalhes_entrada_url_resolves(self):
        url = reverse('detalhes_entrada', args=[1])
        self.assertEqual(resolve(url).func, detalhes_entrada)
    
    def test_excluir_entrada_url_resolves(self):
        url = reverse('excluir_entrada', args=[1])
        self.assertEqual(resolve(url).func, excluir_entrada)
    
    def test_listar_saidas_url_resolves(self):
        url = reverse('listar_saidas')
        self.assertEqual(resolve(url).func, listar_saidas)
    
    def test_adicionar_saida_url_resolves(self):
        url = reverse('adicionar_saida')
        self.assertEqual(resolve(url).func, adicionar_saida)
    
    def test_atualizar_saida_url_resolves(self):
        url = reverse('atualizar_saida', args=[1])
        self.assertEqual(resolve(url).func, atualizar_saida)
    
    def test_detalhes_saida_url_resolves(self):
        url = reverse('detalhes_saida', args=[1])
        self.assertEqual(resolve(url).func, detalhes_saida)
    
    def test_excluir_saida_url_resolves(self):
        url = reverse('excluir_saida', args=[1])
        self.assertEqual(resolve(url).func, excluir_saida)
