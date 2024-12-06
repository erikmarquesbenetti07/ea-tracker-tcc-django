from django.views.generic import ListView, DetailView, CreateView, UpdateView, FormView
from django.shortcuts import get_object_or_404
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from clientes.forms import UsuarioChangeForm, AssociadoCreateForm, AssociadoChangeForm
from usuarios.mixins import LoginClienteMixin
from usuarios.models import Usuario
from empreendimentos.models import Empreendimento, FotoEmpreendimento, DocumentoEmpreendimento, FotoAndamentoObra


class EmpreendimentoListView(LoginClienteMixin, ListView):
    model = Empreendimento
    ordering = ["-id"]
    paginate_by = 100
    login_url = "/login/"
    template_name = "cliente/empreendimentos.html"

    def get_queryset(self) :
            return Empreendimento.objects.filter(usuarios__id=self.request.user.id, visivel=True)


class EmpreendimentoDetailView(LoginClienteMixin, DetailView):
    model = Empreendimento
    ordering = ["-id"]
    paginate_by = 100
    login_url = "/login/"
    template_name = "cliente/empreendimento-detail.html"

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

    def get_success_url(self):
        return reverse_lazy(
            "gestores:empreendimento-foto-update", args=[self.kwargs["pk"]]
        )


class AssociadoListView(LoginClienteMixin, ListView):
    model = Usuario
    ordering = ["-id"]
    paginate_by = 100
    login_url = "/login/"
    template_name = "cliente/associados.html"

    def get_queryset(self) :
            return Usuario.objects.filter(tipo_usuario="ASSOCIADO", cadastrado_por=self.request.user.id)


class AssociadoCreateView(LoginClienteMixin, SuccessMessageMixin, CreateView):
    model = Usuario
    form_class = AssociadoCreateForm
    success_url = "/cliente/associados/"
    success_message = "Associado foi cadastrado"
    login_url = "/login/"
    template_name = "cliente/associado-create.html"


class AssociadoUpdateView(LoginClienteMixin, SuccessMessageMixin, UpdateView):
    model = Usuario
    form_class = AssociadoChangeForm
    success_url = "/cliente/associados/"
    success_message = "Associado foi atualizado"
    login_url = "/login/"
    template_name = "cliente/associado-update.html"


class UsuarioUpdateView(LoginClienteMixin, SuccessMessageMixin, UpdateView):
    model = Usuario
    form_class = UsuarioChangeForm
    success_url = "/cliente/minha-conta/"
    success_message = "Informações atualizadas"
    login_url = "/login/"
    template_name = "cliente/minha-conta.html"

    def get_object(self, queryset=None):
        return self.request.user 
