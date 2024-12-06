from django.urls import path
from . import views


app_name = "associados"

urlpatterns = [
    path("", view=views.EmpreendimentoListView.as_view(), name="empreendimentos"),
    path("empreendimentos/", view=views.EmpreendimentoListView.as_view(), name="empreendimentos-list"),
    path("empreendimento/detalhar/<int:pk>/", view=views.EmpreendimentoDetailView.as_view(), name="empreendimento-detail"),
    path("minha-conta/", view=views.UsuarioUpdateView.as_view(), name="minha-conta"),
]