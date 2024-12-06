from django.shortcuts import render
from django.views.generic.edit import UpdateView
from .models import Empreendimento
from .forms import EmpreendimentoForm

class EmpreendimentoUpdateView(UpdateView):
    model = Empreendimento
    form_class = EmpreendimentoForm
    success_url = "/gestor/empreendimentos/"
    success_message = "Empreendimento foi atualizado"
    login_url = "/login/"
    template_name = "gestor/empreendimento-update.html"
