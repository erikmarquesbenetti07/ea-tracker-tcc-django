# dashboard/api_views.py

from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Count, Avg, Q
from django.http import JsonResponse
from empreendimentos.models import Empreendimento
from usuarios.models import Usuario
from django.db.models.functions import TruncMonth
from django.db.models import Sum
from django.db.models.functions import TruncDate

@api_view(['GET'])
def empreendimentos_por_status(request):
    data = Empreendimento.objects.values('status').annotate(total=Count('status'))
    return Response(data)

@api_view(['GET'])
def empreendimentos_por_cidade(request):
    data = Empreendimento.objects.values('cidade').annotate(total=Count('cidade'))
    return Response(data)

@api_view(['GET'])
def percentual_conclusao(request):
    data = Empreendimento.objects.aggregate(
        terraplanagem=Avg('percentual_terraplanagem'),
        pavimentacao=Avg('percentual_pavimentacao'),
        habitacao=Avg('percentual_habitacao'),
        drenagem=Avg('percentual_drenagem'),
        paisagismo=Avg('percentual_paisagismo'),
        esgoto=Avg('percentual_esgoto_sanitario'),
        agua_potavel=Avg('percentual_agua_potavel'),
        energia_iluminacao=Avg('percentual_energia_iluminacao'),
    )
    return Response(data)

@api_view(['GET'])
def empreendimentos_por_estado(request):
    data = Empreendimento.objects.values('estado').annotate(total=Count('estado'))
    return Response(data)

@api_view(['GET'])
def unidades_por_empreendimento(request):
    data = Empreendimento.objects.values('nome').annotate(total_unidades=Count('numero_unidades'))
    return Response(data)

@api_view(['GET'])
def quantidade_clientes(request):
    # Conta o número de clientes
    total_clientes = Usuario.objects.filter(tipo_usuario="CLIENTE").count()
    return JsonResponse({"total_clientes": total_clientes})

@api_view(['GET'])
def clientes_por_empreendimento(request):
    data = Empreendimento.objects.annotate(
        total_clientes=Count('usuarios', filter=Q(usuarios__tipo_usuario='CLIENTE'))
    ).values('nome', 'total_clientes')
    return Response(data)

@api_view(['GET'])
def novos_clientes_por_mes(request):
    data = Usuario.objects.filter(tipo_usuario="CLIENTE").annotate(
        mes=TruncMonth('date_joined')
    ).values('mes').annotate(total=Count('id')).order_by('mes')

    # Formatar a data para JSON serializable
    data = [{'mes': item['mes'].strftime('%Y-%m'), 'total': item['total']} for item in data]
    return Response(data)

@api_view(['GET'])
def novos_clientes_por_dia(request):
    data = Usuario.objects.filter(tipo_usuario="CLIENTE").annotate(
        dia=TruncDate('date_joined')
    ).values('dia').annotate(total=Count('id')).order_by('dia')

    # Formatar a data para JSON serializable
    data = [{'dia': item['dia'].strftime('%Y-%m-%d'), 'total': item['total']} for item in data]
    return Response(data)