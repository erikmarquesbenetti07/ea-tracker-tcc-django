from django.urls import path
from . import views, api_views

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),
    path('api/empreendimentos/status/', api_views.empreendimentos_por_status, name='empreendimentos_por_status'),
    path('api/empreendimentos/cidade/', api_views.empreendimentos_por_cidade, name='empreendimentos_por_cidade'),
    path('api/percentual/conclusao/', api_views.percentual_conclusao, name='percentual_conclusao'),
    path('api/empreendimentos/estado/', api_views.empreendimentos_por_estado, name='empreendimentos_por_estado'),
    path('api/unidades/empreendimento/', api_views.unidades_por_empreendimento, name='unidades_por_empreendimento'),
    path('api/quantidade/clientes/', api_views.quantidade_clientes, name='quantidade_clientes'),
    path('api/clientes_por_empreendimento/', api_views.clientes_por_empreendimento, name='clientes_por_empreendimento'),
    path('api/novos_clientes_por_mes/', api_views.novos_clientes_por_mes, name='novos_clientes_por_mes'),
    path('api/novos_clientes_por_dia/', api_views.novos_clientes_por_dia, name='novos_clientes_por_dia'),
]
