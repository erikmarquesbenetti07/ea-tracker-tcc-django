from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from usuarios.models import Usuario
from empreendimentos.models import Empreendimento, FotoEmpreendimento, DocumentoEmpreendimento, FotoAndamentoObra


class EmpreendimentoForm(forms.ModelForm):
    class Meta:
        model = Empreendimento
        fields = (
            "nome",
            "numero_unidades",
            "quantidade_blocos",
            "status",
            "logradouro",
            "cidade",
            "estado",
            "link_google_maps",
            "previsao_entrega",
            "estagio",
            "capa",
            'cep',
            "visivel",
        )
        widgets = {
            "status": forms.Select(
                attrs={"class": "form-control"},
            ),
            "estagio": forms.Select(
                attrs={"class": "form-control"},
            ),
            "estado": forms.Select(
                attrs={"class": "form-control"},
            ),
        }


class EmpreendimentoFotoForm(forms.ModelForm):
    class Meta:
        model = FotoEmpreendimento
        fields = ("empreendimento", "imagem")
        widgets = {
            "imagem": forms.ClearableFileInput(
                attrs={
                    "class": "form-control form-control-lg",
                },
            ),
        }


class EmpreendimentoDocumentoForm(forms.ModelForm):
    class Meta:
        model = DocumentoEmpreendimento
        fields = ("empreendimento", "nome_arquivo", "arquivo")
        widgets = {
            "arquivo": forms.ClearableFileInput(
                attrs={
                    "class": "form-control form-control-lg",
                },
            ),
        }
class EmpreendimentoAndamentoObraForm(forms.ModelForm):
    class Meta:
        model = Empreendimento
        fields = (
            "exibe_terraplanagem",
            "percentual_terraplanagem",
            "exibe_pavimentacao",
            "percentual_pavimentacao",
            "exibe_habitacao",
            "percentual_habitacao",
            "exibe_drenagem",
            "percentual_drenagem",
            "exibe_paisagismo",
            "percentual_paisagismo",
            "exibe_esgoto_sanitario",
            "percentual_esgoto_sanitario",
            "exibe_agua_potavel",
            "percentual_agua_potavel",
            "exibe_energia_iluminacao",
            "percentual_energia_iluminacao",
        )
        widgets = {
            "percentual_terraplanagem": forms.TextInput(
                attrs={"class": "form-control w-25"},
            ),
            "percentual_pavimentacao": forms.TextInput(
                attrs={"class": "form-control w-25"},
            ),
            "percentual_habitacao": forms.TextInput(
                attrs={"class": "form-control w-25"},
            ),
            "percentual_drenagem": forms.TextInput(
                attrs={"class": "form-control w-25"},
            ),
            "percentual_paisagismo": forms.TextInput(
                attrs={"class": "form-control w-25"},
            ),
            "percentual_esgoto_sanitario": forms.TextInput(
                attrs={"class": "form-control w-25"},
            ),
            "percentual_agua_potavel": forms.TextInput(
                attrs={"class": "form-control w-25"},
            ),
            "percentual_energia_iluminacao": forms.TextInput(
                attrs={"class": "form-control w-25"},
            )
        }


class EmpreendimentoFotoAndamentoObraForm(forms.ModelForm):
    class Meta:
        model = FotoAndamentoObra
        fields = ("empreendimento", "imagem", "mes")
        widgets = {
            "imagem": forms.ClearableFileInput(
                attrs={
                    "class": "form-control form-control-lg",
                },
            ),
        }



class ClienteCreateForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = (
            "nome_sobrenome", 
            "email",
            "empreendimento",
            "bloco",
            "unidade",
            "tipo_usuario", 
            "telefone", 
            "cidade", 
            "estado", 
            "foto"
        )
        widgets = {
            "empreendimento": forms.Select(
                attrs={"class": "form-control"}
            ),
            "estado": forms.Select(
                attrs={"class": "form-control"},
            ),
        }


class ClienteChangeForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = (
            "nome_sobrenome", 
            "email",
            "empreendimento",
            "bloco",
            "unidade",
            "is_active", 
            "telefone", 
            "cidade", 
            "estado", 
            "foto"
        )
        widgets = {
            "empreendimento": forms.Select(
                attrs={"class": "form-control"}
            ),
            "estado": forms.Select(
                attrs={"class": "form-control"}
            )
        }


class UsuarioChangeForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = (
            "nome_sobrenome", 
            "email", 
            "telefone", 
            "cidade", 
            "estado", 
        )
        widgets = {
            "estado": forms.Select(
                attrs={"class": "form-control"}
            )
        }