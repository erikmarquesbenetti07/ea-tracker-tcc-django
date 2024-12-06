from django import forms
from .models import Empreendimento

class EmpreendimentoForm(forms.ModelForm):
    class Meta:
        model = Empreendimento
        fields = ['nome', 'numero_unidades', 'quantidade_blocos', 'status', 'logradouro', 
                  'cidade', 'estado', 'cep', 'previsao_entrega', 'capa', 'link_google_maps', 'estagio']
