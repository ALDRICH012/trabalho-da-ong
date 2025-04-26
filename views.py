from django.shortcuts import render, redirect
from .forms import AlimentoForm, RoupaForm, HigienePessoalForm
from .models import Alimento, Roupa, HigienePessoal

def home(request):
    return render(request, 'home.html')

def nova_doacao_alimento(request):
    if request.method == 'POST':
        form = AlimentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AlimentoForm()
    return render(request, 'nova_doacao.html', {'form': form, 'tipo': 'alimento'})

def nova_doacao_roupa(request):
    if request.method == 'POST':
        form = RoupaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RoupaForm()
    return render(request, 'nova_doacao.html', {'form': form, 'tipo': 'roupa'})

def nova_doacao_higiene(request):
    if request.method == 'POST':
        form = HigienePessoalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = HigienePessoalForm()
    return render(request, 'nova_doacao.html', {'form': form, 'tipo': 'higiene'})

def lista_doacoes(request):
    alimentos = Alimento.objects.all()
    roupas = Roupa.objects.all()
    higiene = HigienePessoal.objects.all()
    return render(request, 'lista_doacoes.html', {
        'alimentos': alimentos,
        'roupas': roupas,
        'higiene': higiene
    })