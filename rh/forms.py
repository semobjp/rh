from django import forms
from django.db.models import Q
from .models import Filial, Setor, Cargo, Estado, Funcionario

class FilialForm(forms.ModelForm):
	class Meta:
		model = Filial
		fields = '__all__'

class SetorForm(forms.ModelForm):
	class Meta:
		model = Setor
		fields = '__all__'

class CargoForm(forms.ModelForm):
	class Meta:
		model = Cargo
		fields = '__all__'

class EstadoForm(forms.ModelForm):
	class Meta:
		model = Estado
		fields = '__all__'

class FuncionarioForm(forms.ModelForm):
	prefix = "funcionario"

	class Meta:
		model = Funcionario
		exclude = ['user']

class SearchFuncionarioForm(forms.Form):
    nome = forms.CharField(max_length=100, required=False)
    setor = forms.ModelChoiceField(Setor.objects.all(), required=False)

    def clean(self):
        cleaned_data = super(SearchFuncionarioForm, self).clean()
        funcionario = None
        setor = None

        if cleaned_data.get("setor") != None:
        	funcionario = Funcionario.objects.filter(Q(nome__icontains=cleaned_data.get("nome")), Q(setor=cleaned_data.get("setor")))
        else:
        	funcionario = Funcionario.objects.filter(Q(nome__icontains=cleaned_data.get("nome")))

        if self.errors:
            return cleaned_data
        elif not funcionario:
            raise forms.ValidationError("Funcionário não encontrado")

        cleaned_data["nome"] = funcionario.all()

        return cleaned_data