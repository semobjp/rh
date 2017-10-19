from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from django.http import HttpResponseForbidden
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType

from .models import Funcionario
from .forms import FilialForm, SetorForm, CargoForm, EstadoForm, FuncionarioForm, SearchFuncionarioForm

@permission_required('rh.perm_add_rh')
@login_required
def funcionario_new(request):    
    funcionario_form = FuncionarioForm()
    user_form = UserCreationForm(prefix="user")

    if request.method == "POST":
        user_form = UserCreationForm(request.POST, prefix="user")
        funcionario_form = FuncionarioForm(request.POST)

        if user_form.is_valid() and funcionario_form.is_valid():
            user = user_form.save()
            funcionario = funcionario_form.save(commit=False)
            funcionario.user = user       
            funcionario.save()     
            if funcionario.setor.descricao_setor == 'Recursos Humanos':
                group = Group.objects.get(name="rh")
                funcionario.user.groups.add(group)
            messages.success(request, 'Funcionário cadastrado com sucesso.')

    return render(request, 'form_funcionario.html', locals())

@permission_required('rh.perm_add_rh')
@login_required
def filial_new(request):
    if request.method == "POST":
        form = FilialForm(request.POST)
        if form.is_valid():
            filial = form.save(commit=False)
            filial.save()
            messages.success(request, 'Filial cadastrada com sucesso.')
    else:
        form = FilialForm()
    return render(request, 'form_generic.html', {'form': form})

@permission_required('rh.perm_add_rh')
@login_required
def setor_new(request):
    if request.method == "POST":
        form = SetorForm(request.POST)
        if form.is_valid():
            setor = form.save(commit=False)
            setor.save()
            if setor.descricao_setor == 'Recursos Humanos':
                rh, created = Group.objects.get_or_create(name='rh')
                ct = ContentType.objects.get_for_model(Funcionario)
                permission = Permission.objects.create(codename='perm_add_rh',
                                                        name='Permissão Adicionar',
                                                        content_type=ct)
                rh.permissions.add(permission)
            messages.success(request, 'Setor cadastrado com sucesso.')
    else:
        form = SetorForm()
    return render(request, 'form_generic.html', {'form': form})

@permission_required('rh.perm_add_rh')
@login_required
def cargo_new(request):
    if request.method == "POST":
        form = CargoForm(request.POST)
        if form.is_valid():
            cargo = form.save(commit=False)
            cargo.save()
            messages.success(request, 'Cargo cadastrado com sucesso.')
    else:
        form = CargoForm()
    return render(request, 'form_generic.html', {'form': form})

@permission_required('rh.perm_add_rh')
@login_required
def estado_new(request):
    if request.method == "POST":
        form = EstadoForm(request.POST)
        if form.is_valid():
            estado = form.save(commit=False)
            estado.save()
            messages.success(request, 'Estado cadastrado com sucesso.')
    else:
        form = EstadoForm()
    return render(request, 'form_generic.html', {'form': form})

@permission_required('rh.perm_add_rh')
@login_required
def listar(request):
    form = SearchFuncionarioForm()
    funcionario = None
    setor = None
    if request.method == 'POST':
        form = SearchFuncionarioForm(request.POST)
        if form.is_valid():
            funcionario = form.cleaned_data['nome']
            setor = form.cleaned_data['setor']

    return render(request, 'funcionario_list.html', dict(form=form,
                                               funcionario=funcionario,
                                               setor=setor))

@permission_required('rh.perm_add_rh')
@login_required
def editar(request, pk):
    registro = Funcionario.objects.get(pk=pk)
    funcionario_form = FuncionarioForm(instance=registro)

    if request.method == "POST":
        funcionario_form = FuncionarioForm(request.POST, instance=registro)
        if funcionario_form.is_valid():
            funcionario_form.save()
            messages.success(request, 'Funcionário alterado com sucesso.')

    return render(request, 'edit_funcionario.html', locals())

@permission_required('rh.perm_add_rh')
@login_required
def visualizar(request, pk):
    perfil = Funcionario.objects.get(pk=pk)
    registro_user = perfil.user
    return render(request, 'funcionario_detail.html', {'funcionario': perfil, 'user': registro_user})

@login_required
def visualizar_usuario(request):
    perfil = Funcionario.objects.get(user=request.user)
    return render(request, 'funcionario_detail.html', {'funcionario': perfil})

@login_required
def logout(request):
    logout(request)

@login_required
def index(request):
    return render(request, 'index.html')