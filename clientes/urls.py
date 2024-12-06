from django.urls import path
from . import views


app_name = "clientes"

urlpatterns = [
    path("", view=views.EmpreendimentoListView.as_view(), name="empreendimentos"),
    path("empreendimentos/", view=views.EmpreendimentoListView.as_view(), name="empreendimentos-list"),
    path("empreendimento/detalhar/<int:pk>/", view=views.EmpreendimentoDetailView.as_view(), name="empreendimento-detail"),
    path("associados/", view=views.AssociadoListView.as_view(), name="associados"),
    path("associado/cadastrar/", view=views.AssociadoCreateView.as_view(), name="associado-create"),
    path("associado/atualizar/<int:pk>/", view=views.AssociadoUpdateView.as_view(), name="associado-update"),
    path("minha-conta/", view=views.UsuarioUpdateView.as_view(), name="minha-conta"),
]