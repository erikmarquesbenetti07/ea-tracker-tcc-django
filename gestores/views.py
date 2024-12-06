from django.views.generic import ListView, CreateView, UpdateView, FormView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from gestores.forms import ClienteCreateForm, ClienteChangeForm, EmpreendimentoForm, UsuarioChangeForm, EmpreendimentoFotoForm, EmpreendimentoDocumentoForm, EmpreendimentoAndamentoObraForm, EmpreendimentoFotoAndamentoObraForm
from usuarios.mixins import LoginGestorMixin
from usuarios.models import Usuario
from empreendimentos.models import Empreendimento, FotoEmpreendimento, DocumentoEmpreendimento, FotoAndamentoObra
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Count, Avg


class EmpreendimentoListView(LoginGestorMixin, ListView):
    model = Empreendimento
    ordering = ["-id"]
    paginate_by = 100
    login_url = "/login/"
    template_name = "gestor/empreendimentos.html"


class EmpreendimentoCreateView(LoginGestorMixin, SuccessMessageMixin, CreateView):
    model = Empreendimento
    form_class = EmpreendimentoForm
    success_url = "/gestor/empreendimentos/"
    success_message = "Empreendimento foi cadastrado"
    login_url = "/login/"
    template_name = "gestor/empreendimento-create.html"


class EmpreendimentoUpdateView(LoginGestorMixin, SuccessMessageMixin, UpdateView):
    model = Empreendimento
    form_class = EmpreendimentoForm
    success_url = "/gestor/empreendimentos/"
    success_message = "Empreendimento foi atualizado"
    login_url = "/login/"
    template_name = "gestor/empreendimento-update.html"


class EmpreendimentoFotoUpdateView(LoginGestorMixin, SuccessMessageMixin, CreateView):
    model = FotoEmpreendimento
    form_class = EmpreendimentoFotoForm
    success_url = "/gestor/empreendimentos/"
    success_message = "Foto do empreendimento foi cadastrada"
    login_url = "/login/"
    template_name = "gestor/empreendimento-foto-update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        id_empreendimento = self.kwargs["pk"]
        context["id_empreendimento"] = id_empreendimento

        empreendimento = get_object_or_404(Empreendimento, pk=id_empreendimento)
        context["empreendimento"] = empreendimento

        fotos = FotoEmpreendimento.objects.filter(empreendimento=id_empreendimento)
        context["fotos"] = fotos

        return context

    def get_success_url(self):
        return reverse_lazy(
            "gestores:empreendimento-foto-update", args=[self.kwargs["pk"]]
        )


class EmpreendimentoFotoDeleteView(LoginGestorMixin, SuccessMessageMixin, DeleteView):
    model = FotoEmpreendimento
    success_url = "/gestor/empreendimentos/"
    success_message = "Foto do empreendimento foi deletada"
    login_url = "/login/"
    template_name = "gestor/empreendimento-foto-delete.html"

    def get_success_url(self):
        empreendimento = self.object.empreendimento.id
        return reverse_lazy(
            "gestores:empreendimento-foto-update", args=[empreendimento]
        )
    

class EmpreendimentoDocumentoUpdateView(LoginGestorMixin, SuccessMessageMixin, CreateView):
    model = DocumentoEmpreendimento
    form_class = EmpreendimentoDocumentoForm
    success_url = "/gestor/empreendimentos/"
    success_message = "Documento do empreendimento foi cadastrado"
    login_url = "/login/"
    template_name = "gestor/empreendimento-documento-update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        id_empreendimento = self.kwargs["pk"]
        context["id_empreendimento"] = id_empreendimento

        empreendimento = get_object_or_404(Empreendimento, pk=id_empreendimento)
        context["empreendimento"] = empreendimento

        documentos = DocumentoEmpreendimento.objects.filter(empreendimento=id_empreendimento)
        context["documentos"] = documentos

        return context

    def get_success_url(self):
        return reverse_lazy(
            "gestores:empreendimento-documento-update", args=[self.kwargs["pk"]]
        )


class EmpreendimentoDocumentoDeleteView(LoginGestorMixin, SuccessMessageMixin, DeleteView):
    model = DocumentoEmpreendimento
    success_url = "/gestor/empreendimentos/"
    success_message = "Documento do empreendimento foi deletado"
    login_url = "/login/"
    template_name = "gestor/empreendimento-documento-delete.html"

    def get_success_url(self):
        empreendimento = self.object.empreendimento.id
        return reverse_lazy(
            "gestores:empreendimento-documento-update", args=[empreendimento]
        )
    

class EmpreendimentoAndamentoObraUpdateView(LoginGestorMixin, SuccessMessageMixin, UpdateView):
    model = Empreendimento
    form_class = EmpreendimentoAndamentoObraForm
    success_url = "/gestor/empreendimentos/"
    success_message = "Andamento da obra foi atualizado"
    login_url = "/login/"
    template_name = "gestor/empreendimento-andamento-obra-update.html"


class EmpreendimentoFotoAndamentoObraUpdateView(LoginGestorMixin, SuccessMessageMixin, CreateView):
    model = FotoAndamentoObra
    form_class = EmpreendimentoFotoAndamentoObraForm
    success_url = "/gestor/empreendimentos/"
    success_message = "Foto do andamento foi cadastrada"
    login_url = "/login/"
    template_name = "gestor/empreendimento-foto-andamento-obra-update.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        id_empreendimento = self.kwargs["pk"]
        context["id_empreendimento"] = id_empreendimento

        empreendimento = get_object_or_404(Empreendimento, pk=id_empreendimento)
        context["empreendimento"] = empreendimento

        fotos = FotoAndamentoObra.objects.filter(empreendimento=id_empreendimento)
        context["fotos"] = fotos

        return context

    def get_success_url(self):
        return reverse_lazy(
            "gestores:empreendimento-foto-andamento-update", args=[self.kwargs["pk"]]
        )


class EmpreendimentoFotoAndamentoObraDeleteView(LoginGestorMixin, SuccessMessageMixin, DeleteView):
    model = FotoAndamentoObra
    success_url = "/gestor/empreendimentos/"
    success_message = "Foto andamento obra foi deletada"
    login_url = "/login/"
    template_name = "gestor/empreendimento-foto-andamento-obra-delete.html"

    def get_success_url(self):
        empreendimento = self.object.empreendimento.id
        return reverse_lazy(
            "gestores:empreendimento-foto-andamento-update", args=[empreendimento]
        )
    

class ClienteListView(LoginGestorMixin, ListView):
    model = Usuario
    queryset = Usuario.objects.filter(tipo_usuario="CLIENTE")
    ordering = ["-id"]
    paginate_by = 100
    login_url = "/login/"
    template_name = "gestor/clientes.html"


class ClienteCreateView(LoginGestorMixin, SuccessMessageMixin, CreateView):
    model = Usuario
    form_class = ClienteCreateForm
    success_url = "/gestor/clientes/"
    success_message = "Cliente foi cadastrado"
    login_url = "/login/"
    template_name = "gestor/cliente-create.html"


class ClienteUpdateView(LoginGestorMixin, SuccessMessageMixin, UpdateView):
    model = Usuario
    form_class = ClienteChangeForm
    success_url = "/gestor/clientes/"
    success_message = "Cliente foi atualizado"
    login_url = "/login/"
    template_name = "gestor/cliente-update.html"


class UsuarioUpdateView(LoginGestorMixin, SuccessMessageMixin, UpdateView):
    model = Usuario
    form_class = UsuarioChangeForm
    success_url = "/gestor/minha-conta/"
    success_message = "Informações atualizadas"
    login_url = "/login/"
    template_name = "gestor/minha-conta.html"

    def get_object(self, queryset=None):
        return self.request.user 
    
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Avg
from empreendimentos.models import Empreendimento

@login_required
def dashboard_view(request):
    # Dados que serão usados nos gráficos
    empreendimentos_por_status = Empreendimento.objects.values('status').annotate(total=Count('status'))
    empreendimentos_por_cidade = Empreendimento.objects.values('cidade').annotate(total=Count('cidade'))
    empreendimentos_por_estado = Empreendimento.objects.values('estado').annotate(total=Count('estado'))
    percentuais_conclusao = Empreendimento.objects.aggregate(
        terraplanagem=Avg('percentual_terraplanagem'),
        pavimentacao=Avg('percentual_pavimentacao'),
        habitacao=Avg('percentual_habitacao'),
        drenagem=Avg('percentual_drenagem'),
        paisagismo=Avg('percentual_paisagismo'),
        esgoto=Avg('percentual_esgoto_sanitario'),
        agua_potavel=Avg('percentual_agua_potavel'),
        energia_iluminacao=Avg('percentual_energia_iluminacao'),
    )

    context = {
        'empreendimentos_por_status': list(empreendimentos_por_status),
        'empreendimentos_por_cidade': list(empreendimentos_por_cidade),
        'empreendimentos_por_estado': list(empreendimentos_por_estado),
        'percentuais_conclusao': percentuais_conclusao,
    }
    return render(request, 'dashboard/dashboard.html', context)
