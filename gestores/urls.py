from django.urls import path, include
from . import views

app_name = "gestores"

urlpatterns = [
    path("", view=views.EmpreendimentoListView.as_view(), name="empreendimentos"),
    path("empreendimentos/", view=views.EmpreendimentoListView.as_view(), name="empreendimentos"),
    path("empreendimento/cadastrar/", view=views.EmpreendimentoCreateView.as_view(), name="empreendimento-create"),
    path("empreendimento/atualizar/<int:pk>/", view=views.EmpreendimentoUpdateView.as_view(), name="empreendimento-update"),
    path("empreendimento/foto/atualizar/<int:pk>/", view=views.EmpreendimentoFotoUpdateView.as_view(), name="empreendimento-foto-update"),
    path("empreendimento/foto/deletar/<int:pk>/", view=views.EmpreendimentoFotoDeleteView.as_view(), name="empreendimento-foto-delete"),
    path("empreendimento/documento/atualizar/<int:pk>/", view=views.EmpreendimentoDocumentoUpdateView.as_view(), name="empreendimento-documento-update"),
    path("empreendimento/documento/deletar/<int:pk>/", view=views.EmpreendimentoDocumentoDeleteView.as_view(), name="empreendimento-documento-delete"),
    path("empreendimento/andamento-obra/atualizar/<int:pk>/", view=views.EmpreendimentoAndamentoObraUpdateView.as_view(), name="empreendimento-andamento-obra-update"),
    path("empreendimento/foto-andamento-obra/atualizar/<int:pk>/", view=views.EmpreendimentoFotoAndamentoObraUpdateView.as_view(), name="empreendimento-foto-andamento-update"),
    path("empreendimento/foto-andamento-obra/deletar/<int:pk>/", view=views.EmpreendimentoFotoAndamentoObraDeleteView.as_view(), name="empreendimento-foto-andamento-delete"),
    path("clientes/", view=views.ClienteListView.as_view(), name="clientes"),
    path("cliente/cadastrar/", view=views.ClienteCreateView.as_view(), name="cliente-create"),
    path("cliente/atualizar/<int:pk>/", view=views.ClienteUpdateView.as_view(), name="cliente-update"),
    path("minha-conta/", view=views.UsuarioUpdateView.as_view(), name="minha-conta"),
    path("dashboard/", views.dashboard_view, name="dashboard"),
    path("dashboard/api/", include("dashboard.urls", namespace="dashboard")),  # Corrigido para 'dashboard'
]
