from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto, Fornecedor, Categoria, Entrada, Saida
from .forms import ProdutoForm, FornecedorForm, CategoriaForm, EntradaForm, SaidaForm, RegistroUsuarioForm
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# -----------------------------views relacionadas aos produtos-----------------------------

@login_required
def listar_produtos(request):
    produtos = Produto.objects.all().order_by('nome')
    paginator = Paginator(produtos, 20)  # Exibe 20 produtos por página
    page_number = request.GET.get('page')  # Obtém o número da página atual a partir dos parâmetros da URL
    page_obj = paginator.get_page(page_number)  # Obtém os produtos para a página atual
    return render(request, 'listar_produtos.html', {'page_obj': page_obj})

@login_required
def adicionar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_produtos')
    else:
        form = ProdutoForm()
        return render(request, 'adicionar_produto.html', {'form': form})

@login_required
def atualizar_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)

    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('listar_produtos')
    else:
        form = ProdutoForm(instance=produto)
        return render(request, 'atualizar_produto.html', {'form': form, 'produto': produto})

@login_required
def detalhes_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    return render(request, 'detalhes_produto.html', {'produto': produto})

@login_required
def excluir_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method in ['POST', 'GET']:
        produto.delete()
        return redirect('listar_produtos')

# -----------------------------views relacionadas aos fornecedores-----------------------------

@login_required
def listar_fornecedores(request):
    fornecedores = Fornecedor.objects.all().order_by('nome')
    paginator = Paginator(fornecedores, 20)  # Exibe 20 fornecedores por página
    page_number = request.GET.get('page')  # Obtém o número da página atual a partir dos parâmetros da URL
    page_obj = paginator.get_page(page_number)  # Obtém os fornecedores para a página atual
    return render(request, 'listar_fornecedores.html', {'page_obj': page_obj})

@login_required
def adicionar_fornecedor(request):
    if request.method == 'POST':
        form = FornecedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_fornecedores')
    else:
        form = FornecedorForm()
        return render(request, 'adicionar_fornecedor.html', {'form': form})

@login_required
def atualizar_fornecedor(request, pk):
    fornecedor = get_object_or_404(Fornecedor, pk=pk)

    if request.method == 'POST':
        form = FornecedorForm(request.POST, instance=fornecedor)
        if form.is_valid():
            form.save()
            return redirect('listar_fornecedores')
    else:
        form = FornecedorForm(instance=fornecedor)
        return render(request, 'atualizar_fornecedor.html', {'form': form, 'fornecedor': fornecedor})

@login_required
def detalhes_fornecedor(request, pk):
    fornecedor = get_object_or_404(Fornecedor, pk=pk)
    return render(request, 'detalhes_fornecedor.html', {'fornecedor': fornecedor})

@login_required
def excluir_fornecedor(request, pk):
    fornecedor = get_object_or_404(Fornecedor, pk=pk)
    if request.method in ['POST', 'GET']:
        fornecedor.delete()
        return redirect('listar_fornecedores')

# -----------------------------views relacionadas as categorias-----------------------------

@login_required
def listar_categorias(request):
    categorias = Categoria.objects.all().order_by('nome')
    paginator = Paginator(categorias, 20)  
    page_number = request.GET.get('page')  # Obtém o número da página atual a partir dos parâmetros da URL
    page_obj = paginator.get_page(page_number)  
    return render(request, 'listar_categorias.html', {'page_obj': page_obj})

@login_required
def adicionar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_categorias')
    else:
        form = CategoriaForm()
        return render(request, 'adicionar_categoria.html', {'form': form})

@login_required
def atualizar_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)

    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('listar_categorias')
    else:
        form = CategoriaForm(instance=categoria)
        return render(request, 'atualizar_categoria.html', {'form': form, 'categoria': categoria})

@login_required
def detalhes_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    return render(request, 'detalhes_categoria.html', {'categoria': categoria})

@login_required
def excluir_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    if request.method in ['POST', 'GET']:
        categoria.delete()
        return redirect('listar_categorias')

# -----------------------------views relacionadas as entradas-----------------------------

@login_required
def listar_entradas(request):
    entradas = Entrada.objects.all().order_by('-data')  # Exibe as entradas mais recentes primeiro
    paginator = Paginator(entradas, 20)  # Exibe 20 entradas por página
    page_number = request.GET.get('page')  # Obtém o número da página atual a partir dos parâmetros da URL
    page_obj = paginator.get_page(page_number)  # Obtém os entradas para a página atual
    return render(request, 'listar_entradas.html', {'page_obj': page_obj})

@login_required
def adicionar_entrada(request):
    if request.method == 'POST':
        form = EntradaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_entradas')
    else:
        form = EntradaForm()
        return render(request, 'adicionar_entrada.html', {'form': form})

@login_required
def atualizar_entrada(request, pk):
    entrada = get_object_or_404(Entrada, pk=pk)

    if request.method == 'POST':
        form = EntradaForm(request.POST, instance=entrada)
        if form.is_valid():
            form.save()
            return redirect('listar_entradas')
    else:
        form = EntradaForm(instance=entrada)
        return render(request, 'atualizar_entrada.html', {'form': form, 'entrada': entrada})

@login_required
def detalhes_entrada(request, pk):
    entrada = get_object_or_404(Entrada, pk=pk)
    return render(request, 'detalhes_entrada.html', {'entrada': entrada})

@login_required
def excluir_entrada(request, pk):
    entrada = get_object_or_404(Entrada, pk=pk)
    if request.method in ['POST', 'GET']:
        entrada.delete()
        return redirect('listar_entradas')

# -----------------------------views relacionadas as saidas-----------------------------

@login_required
def listar_saidas(request):
    saidas = Saida.objects.all().order_by('-data')  # Exibe as saidas mais recentes primeiro
    paginator = Paginator(saidas, 20)  # Exibe 20 saidas por página
    page_number = request.GET.get('page')  # Obtém o número da página atual a partir dos parâmetros da URL
    page_obj = paginator.get_page(page_number)  # Obtém os saidas para a página atual
    return render(request, 'listar_saidas.html', {'page_obj': page_obj})

@login_required
def adicionar_saida(request):
    if request.method == 'POST':
        form = SaidaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_saidas')
    else:
        form = SaidaForm()
        return render(request, 'adicionar_saida.html', {'form': form})
    
@login_required
def atualizar_saida(request, pk):
    saida = get_object_or_404(Saida, pk=pk)

    if request.method == 'POST':
        form = SaidaForm(request.POST, instance=saida)
        if form.is_valid():
            form.save()
            return redirect('listar_saidas')
    else:
        form = SaidaForm(instance=saida)
        return render(request, 'atualizar_saida.html', {'form': form, 'saida': saida})

@login_required
def detalhes_saida(request, pk):
    saida = get_object_or_404(Saida, pk=pk)
    return render(request, 'detalhes_saida.html', {'saida': saida})

@login_required
def excluir_saida(request, pk):
    saida = get_object_or_404(Saida, pk=pk)
    if request.method in ['POST', 'GET']:
        saida.delete()
        return redirect('listar_saidas')  
 

# -----------------------------outras views para controle de usuarios-----------------------------


def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('listar_produtos')
        else:
            messages.error(request, 'Usuário ou senha incorretos.' )
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

@login_required
def custom_logout(request):
    logout(request)
    return redirect('login')

@login_required
def perfil_usuario(request):
    return render(request, 'perfil.html')

def registro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário registrado com sucesso! Você já pode fazer login.')
            return redirect('login')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'registro.html', {'form': form})




