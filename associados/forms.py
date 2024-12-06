from django import forms
from django.contrib.auth.forms import UserChangeForm
from usuarios.models import Usuario


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