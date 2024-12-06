import uuid
from datetime import datetime, timedelta
from django.db import models
from django.contrib.auth.models import AbstractUser
from random import randint
from .managers import UserManager
from empreendimentos.models import Empreendimento

# Constantes para tipos de usuário e estados brasileiros
TIPOS_USUARIOS = [
    ("GESTOR", "Gestor"),
    ("CLIENTE", "Cliente"),
    ("ASSOCIADO", "Associado"),
]

ESTADOS_BRASILEIROS = [
    ("AC", "Acre"),
    ("AL", "Alagoas"),
    ("AP", "Amapá"),
    ("AM", "Amazonas"),
    ("BA", "Bahia"),
    ("CE", "Ceará"),
    ("DF", "Distrito Federal"),
    ("ES", "Espírito Santo"),
    ("GO", "Goiás"),
    ("MA", "Maranhão"),
    ("MT", "Mato Grosso"),
    ("MS", "Mato Grosso do Sul"),
    ("MG", "Minas Gerais"),
    ("PA", "Pará"),
    ("PB", "Paraíba"),
    ("PR", "Paraná"),
    ("PE", "Pernambuco"),
    ("PI", "Piauí"),
    ("RJ", "Rio de Janeiro"),
    ("RN", "Rio Grande do Norte"),
    ("RS", "Rio Grande do Sul"),
    ("RO", "Rondônia"),
    ("RR", "Roraima"),
    ("SC", "Santa Catarina"),
    ("SP", "São Paulo"),
    ("SE", "Sergipe"),
    ("TO", "Tocantins"),
]

class Usuario(AbstractUser):
    # Campos adicionais para o usuário
    username = None  # Usamos o email como o campo USERNAME_FIELD
    email = models.EmailField(unique=True)
    tipo_usuario = models.CharField(max_length=20, choices=TIPOS_USUARIOS)
    nome_sobrenome = models.CharField(max_length=60)
    telefone = models.CharField(max_length=15)
    cidade = models.CharField(max_length=80, null=True, blank=True)
    estado = models.CharField(max_length=2, choices=ESTADOS_BRASILEIROS, default="AC")
    foto = models.ImageField(upload_to="foto/%Y/%m/%d", default="usuario-padrao.png", null=True, blank=True)
    bloco = models.CharField(max_length=20, null=True, blank=True)
    unidade = models.CharField(max_length=20, null=True, blank=True)
    cadastrado_por = models.CharField(max_length=20, null=True, blank=True)
    empreendimento = models.ForeignKey(
        Empreendimento,
        related_name='usuarios',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    # Campos para recuperação de senha via SMS
    codigo_verificacao = models.CharField(max_length=6, null=True, blank=True)
    codigo_expiracao = models.DateTimeField(null=True, blank=True)

    # Configuração de campos para o AbstractUser
    USERNAME_FIELD = "email"  # Definimos o email como identificador principal
    REQUIRED_FIELDS = []  # Outros campos necessários para criação de superusuários

    objects = UserManager()  # Utilizando um manager customizado

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

    def __str__(self):
        return self.nome_sobrenome

    @property
    def usuario_ativo(self):
        """Retorna o status do usuário ('Ativo' ou 'Inativo')."""
        return "Ativo" if self.is_active else "Inativo"

    def gerar_codigo_verificacao(self):
        """Gera um código de verificação de 6 dígitos e define o tempo de expiração para 5 minutos a partir da geração."""
        codigo = f"{randint(100000, 999999)}"
        self.codigo_verificacao = codigo
        self.codigo_expiracao = datetime.now() + timedelta(minutes=5)
        self.save()
        return codigo

    def codigo_esta_valido(self):
        """Verifica se o código ainda está dentro do tempo de validade."""
        return datetime.now() < self.codigo_expiracao if self.codigo_expiracao else False
