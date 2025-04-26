from django import forms
from .models import Alimento, Roupa, HigienePessoal

class AlimentoForm(forms.ModelForm):
    class Meta:
        model = Alimento
        fields = ['nome', 'quantidade', 'data_validade']
        widgets = {
            'data_validade': forms.DateInput(attrs={'type': 'date'})
        }

class RoupaForm(forms.ModelForm):
    class Meta:
        model = Roupa
        fields = ['tipo', 'tamanho', 'quantidade']

class HigienePessoalForm(forms.ModelForm):
    class Meta:
        model = HigienePessoal
        fields = ['tipo', 'quantidade'] 