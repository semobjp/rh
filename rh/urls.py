from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^funcionarios/cadastro$', views.funcionario_new, name='funcionario_new'),
    url(r'^funcionarios/listar$', views.listar, name='listar'),
    url(r'^funcionarios/editar/(?P<pk>\d+)/$', views.editar, name='editar'),
    url(r'^funcionarios/visualizar/(?P<pk>\d+)/$', views.visualizar, name='visualizar'),
    url(r'^filial/$', views.filial_new, name='filial_new'),
    url(r'^setor/$', views.setor_new, name='setor_new'),
    url(r'^cargo/$', views.cargo_new, name='cargo_new'),
    url(r'^estado/$', views.estado_new, name='estado_new'),
]