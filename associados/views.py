from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, UpdateView
from associados.forms import UsuarioChangeForm
from usuarios.mixins import LoginAssociadoMixin
from usuarios.models import Usuario
from empreendimentos.models import Empreendimento, FotoEmpreendimento, DocumentoEmpreendimento, FotoAndamentoObra

class EmpreendimentoListView(LoginAssociadoMixin, ListView):
    model = Empreendimento
    ordering = ["-id"]
    paginate_by = 100
    login_url = "/login/"
    template_name = "associado/empreendimentos.html"

    def get_queryset(self) :
            return Empreendimento.objects.filter(usuario__id=self.request.user.id, visivel=True)


class EmpreendimentoDetailView(LoginAssociadoMixin, DetailView):
    model = Empreendimento
    ordering = ["-id"]
    paginate_by = 100
    login_url = "/login/"
    template_name = "associado/empreendimento-detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        id_empreendimento = self.kwargs["pk"]
        context["id_empreendimento"] = id_empreendimento

        empreendimento = get_object_or_404(Empreendimento, pk=id_empreendimento)
        context["empreendimento"] = empreendimento

        fotos = FotoEmpreendimento.objects.filter(empreendimento=id_empreendimento)
        context["fotos"] = fotos

        documentos = DocumentoEmpreendimento.objects.filter(empreendimento=id_empreendimento)
        context["documentos"] = documentos

        fotos_andamento_obra = FotoAndamentoObra.objects.filter(empreendimento=id_empreendimento)
        context["fotos_andamento_obra"] = fotos_andamento_obra

        percentuais = []
        if empreendimento.exibe_terraplanagem:
            percentuais.append(int(empreendimento.percentual_terraplanagem))
        if empreendimento.exibe_pavimentacao:
            percentuais.append(int(empreendimento.percentual_pavimentacao))
        if empreendimento.exibe_habitacao:
            percentuais.append(int(empreendimento.percentual_habitacao))
        if empreendimento.exibe_drenagem:
            percentuais.append(int(empreendimento.percentual_drenagem))
        if empreendimento.exibe_paisagismo:
            percentuais.append(int(empreendimento.percentual_paisagismo))
        if empreendimento.exibe_esgoto_sanitario:
            percentuais.append(int(empreendimento.percentual_esgoto_sanitario))
        if empreendimento.exibe_agua_potavel:
            percentuais.append(int(empreendimento.percentual_agua_potavel))
        if empreendimento.exibe_energia_iluminacao:
            percentuais.append(int(empreendimento.percentual_energia_iluminacao))
        if len(percentuais) > 0:
            context["andamento_obra"] = int(sum(percentuais) / len(percentuais))
        else:
            context["andamento_obra"] = 0
        return context
    

class UsuarioUpdateView(LoginAssociadoMixin, SuccessMessageMixin, UpdateView):
    model = Usuario
    form_class = UsuarioChangeForm
    success_url = "/associado/minha-conta/"
    success_message = "Informações atualizadas"
    login_url = "/login/"
    template_name = "associado/minha-conta.html"

    def get_object(self, queryset=None):
        return self.request.user 