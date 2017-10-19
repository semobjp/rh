from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Filial(models.Model):
	descricao_filial = models.CharField(max_length=100)

	def __str__(self):
		return self.descricao_filial

class Setor(models.Model):
	descricao_setor = models.CharField(max_length=100)
	
	def __str__(self):
		return self.descricao_setor

class Cargo(models.Model):
	descricao_cargo = models.CharField(max_length=100)
	
	def __str__(self):
		return self.descricao_cargo

class Estado(models.Model):
	descricao_estado = models.CharField(max_length=100)
	
	def __str__(self):
		return self.descricao_estado

class Funcionario(models.Model):    
	VINCULO_CHOICES = (
		('', '-'),
		('Ativo', 'Ativo'),
		('Desativado', 'Desativado'),
		)   
	CIVIL_CHOICES = (
		('', '-'),
		('Solteiro', 'Solteiro'),
		('Casado', 'Casado'),
		('Viúvo', 'Viúvo'),
		)
	user = models.OneToOneField(User)
	nome = models.CharField(max_length=100)
	nascimento = models.DateField()
	cpf = models.CharField(unique=True, max_length=20)
	filial = models.ForeignKey(Filial, on_delete=models.CASCADE)
	setor = models.ForeignKey(Setor, on_delete=models.CASCADE)
	vinculo = models.CharField(max_length=50, choices=VINCULO_CHOICES)
	cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
	mae = models.CharField(max_length=100)
	pai = models.CharField(max_length=100)	
	estado_civil = models.CharField(max_length=50, choices=CIVIL_CHOICES)
	laudo = models.TextField()
	rua = models.CharField(max_length=100)
	numero = models.CharField(max_length=10)
	bairro = models.CharField(max_length=100)
	cep = models.CharField(max_length=20)
	cidade = models.CharField(max_length=100)
	estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

	def __str__(self):
		return "Perfil do usuário: {}".format(self.user.pk)