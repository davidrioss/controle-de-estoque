from django.urls import path
from .views import *

urlpatterns = [
    path('', custom_login, name='login'),
    path('produtos/', listar_produtos, name='listar_produtos'),
    path('produtos/adicionar/', adicionar_produto, name='adicionar_produto'),
    path('produtos/editar/<int:pk>/', atualizar_produto, name='atualizar_produto'), 
    path('produtos/detalhes/<int:pk>/', detalhes_produto, name='detalhes_produto'), 
    path('produtos/excluir/<int:pk>/', excluir_produto, name='excluir_produto'),
    path('entradas/', listar_entradas, name='listar_entradas'),
    path('entradas/adicionar/', adicionar_entrada, name='adicionar_entrada'),
    path('entradas/editar/<int:pk>/', atualizar_entrada, name='atualizar_entrada'),
    path('entradas/detalhes/<int:pk>/', detalhes_entrada, name='detalhes_entrada'),
    path('entradas/excluir/<int:pk>/', excluir_entrada, name='excluir_entrada'),
    path('saidas/', listar_saidas, name='listar_saidas'),
    path('saidas/adicionar/', adicionar_saida, name='adicionar_saida'),
    path('saidas/editar/<int:pk>/', atualizar_saida, name='atualizar_saida'),
    path('saidas/detalhes/<int:pk>/', detalhes_saida, name='detalhes_saida'),
    path('saidas/excluir/<int:pk>/', excluir_saida, name='excluir_saida'),
    path('categorias/', listar_categorias, name='listar_categorias'),
    path('categorias/adicionar/', adicionar_categoria, name='adicionar_categoria'),
    path('categorias/editar/<int:pk>/', atualizar_categoria, name='atualizar_categoria'),
    path('categorias/detalhes/<int:pk>/', detalhes_categoria, name='detalhes_categoria'),
    path('categorias/excluir/<int:pk>/', excluir_categoria, name='excluir_categoria'),
    path('fornecedores/', listar_fornecedores, name='listar_fornecedores'),
    path('fornecedores/adicionar/', adicionar_fornecedor, name='adicionar_fornecedor'),
    path('fornecedores/editar/<int:pk>/', atualizar_fornecedor, name='atualizar_fornecedor'),
    path('fornecedores/detalhes/<int:pk>/', detalhes_fornecedor, name='detalhes_fornecedor'),
    path('fornecedores/excluir/<int:pk>/', excluir_fornecedor, name='excluir_fornecedor'),
    path('login/', custom_login, name='login'),
    path('logout/', custom_logout, name='logout'),
    path('perfil/', perfil_usuario, name='perfil_usuario'),
    path('registro/', registro, name='registro'),
    
]

