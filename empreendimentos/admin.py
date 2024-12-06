from django.contrib import admin
from .models import Empreendimento, FotoEmpreendimento, DocumentoEmpreendimento, FotoAndamentoObra

admin.site.register(Empreendimento)
admin.site.register(FotoEmpreendimento)
admin.site.register(DocumentoEmpreendimento)
admin.site.register(FotoAndamentoObra)