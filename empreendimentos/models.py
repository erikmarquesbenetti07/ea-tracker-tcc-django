from django.db import models


STATUS = [
    ('PRELANCAMENTO', 'Pré-lançamento'),
    ('LANCAMENTO', 'Lançamento'),
    ('EMCONTRUCAO', 'Em Construção'),
]
ESTAGIOS = [
    ('OBRNAOINICIADA', 'Obras não iniciadas'),
    ('OBREMANDAMENTO', 'Obras em andamento'),
    ('OBRFINALIZADAS', 'Obras finalizadas'),
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
CATEGORIAS = [
    ('AGUAPOTAVEL', 'Água Potável'),
    ('ENERGIAILUMINACAO', 'Energia e Iluminação'),
    ('DRENAGEM', 'Drenagem'),
    ('ALVENARIA', 'Alvenaria'),
    ('ACABAMENTO', 'Acabamento'),
]

class Empreendimento(models.Model):    
    nome = models.CharField(max_length=200)
    numero_unidades = models.CharField(max_length=10)
    unidades_disponiveis = models.IntegerField(default=0)
    cep = models.CharField(max_length=9, blank=True, null=True)
    quantidade_blocos = models.CharField(
        max_length=10,
        null=True,
        blank=True,
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS,
        default='PRELANCAMENTO',
    )
    logradouro = models.CharField(max_length=200)
    cidade = models.CharField(max_length=200)
    estado = models.CharField(
        max_length=2,
        choices=ESTADOS_BRASILEIROS,
        default="AC"
    )
    link_google_maps = models.TextField()
    previsao_entrega = models.DateField()
    estagio = models.CharField(
        max_length=20,
        choices=ESTAGIOS,
        default='OBRNAOINICIADA',
    )
    visivel = models.BooleanField(default=False)
    percentual_terraplanagem = models.CharField(max_length=3, default=0)
    exibe_terraplanagem = models.BooleanField(default=False)

    percentual_pavimentacao = models.CharField(max_length=3, default=0)
    exibe_pavimentacao = models.BooleanField(default=False)

    percentual_habitacao = models.CharField(max_length=3, default=0)
    exibe_habitacao = models.BooleanField(default=False)

    percentual_drenagem = models.CharField(max_length=3, default=0)
    exibe_drenagem = models.BooleanField(default=False)

    percentual_paisagismo = models.CharField(max_length=3, default=0)
    exibe_paisagismo = models.BooleanField(default=False)

    percentual_esgoto_sanitario = models.CharField(max_length=3, default=0)
    exibe_esgoto_sanitario = models.BooleanField(default=False)

    percentual_agua_potavel = models.CharField(max_length=3, default=0)
    exibe_agua_potavel = models.BooleanField(default=False)

    percentual_energia_iluminacao = models.CharField(max_length=3, default=0)
    exibe_energia_iluminacao = models.BooleanField(default=False)

    capa = models.ImageField(
        upload_to='empreendimento/capa/',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Empreendimento"
        verbose_name_plural = "Empreendimentos"

    @property
    def status_empreendimento(self):
        if self.status == "LANCAMENTO":
            status = "Lançamento"
        elif self.status == "EMCONTRUCAO":
            status = "Em Construção"
        else:
            status = "Pré-lançamento"
        return status
    

    @property
    def estagio_empreendimento(self):
        if self.estagio == "OBREMANDAMENTO":
            estagio = "Obras em andamento"
        elif self.estagio == "OBRFINALIZADAS":
            estagio = "Obras finalizadas"
        else:
            estagio = "Obras não iniciadas"
        return estagio
    

class FotoEmpreendimento(models.Model):
    empreendimento = models.ForeignKey(
        Empreendimento,
        verbose_name="Empreendimento",
        on_delete=models.CASCADE,
    )
    imagem = models.ImageField(
        upload_to='empreendimento/foto/',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = "Foto Empreendimento"
        verbose_name_plural = "Fotos Empreendimentos"

    def __str__(self):
        return f"{self.id}"


class DocumentoEmpreendimento(models.Model):
    empreendimento = models.ForeignKey(
        Empreendimento,
        verbose_name="Empreendimento",
        on_delete=models.CASCADE,
    )
    nome_arquivo = models.CharField(max_length=60)
    arquivo = models.FileField(
        upload_to='empreendimento/documento/',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = "Documento Empreendimento"
        verbose_name_plural = "Documentos Empreendimentos"

    def __str__(self):
        return f"{self.id}"


class FotoAndamentoObra(models.Model):
    empreendimento = models.ForeignKey(
        Empreendimento,
        verbose_name="Empreendimento",
        on_delete=models.CASCADE,
    )
    mes = models.CharField(max_length=20)
    imagem = models.ImageField(
        upload_to='empreendimento/obra/',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = "Foto Andamento Obra"
        verbose_name_plural = "Fotos Andamento Obras"

    def __str__(self):
        return f"{self.id}"