from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from usuarios.models import Usuario


class AssociadoCreateForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = (
            "empreendimento",
            "nome_sobrenome", 
            "email",
            "empreendimento", 
            "tipo_usuario", 
            "telefone", 
            "cidade", 
            "estado", 
            "foto",
            "cadastrado_por"
        )
        widgets = {
            "empreendimento": forms.Select(
                attrs={"class": "form-control"},
            ),
            "estado": forms.Select(
                attrs={"class": "form-control"}
            ),
        }


class AssociadoChangeForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = (
            "nome_sobrenome", 
            "email", 
            "is_active", 
            "telefone", 
            "cidade", 
            "estado", 
            "foto"
        )
        widgets = {
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