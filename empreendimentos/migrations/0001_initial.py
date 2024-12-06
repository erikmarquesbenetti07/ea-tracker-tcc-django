# Generated by Django 5.1.1 on 2024-09-06 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empreendimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('numero_unidades', models.CharField(max_length=10)),
                ('status', models.CharField(choices=[('PRELANCAMENTO', 'Pré-lançamento'), ('LANCAMENTO', 'Lançamento'), ('EMCONTRUCAO', 'Em Construção')], default='PRELANCAMENTO', max_length=20)),
                ('logradouro', models.CharField(max_length=200)),
                ('cidade', models.CharField(max_length=200)),
                ('estado', models.CharField(max_length=2)),
                ('previsao_entrega', models.DateField()),
                ('estagio', models.CharField(choices=[('OBRNAOINICIADA', 'Obras não iniciadas'), ('OBREMANDAMENTO', 'Obras em andamento'), ('OBRFINALIZADS', 'Obras finalizadas')], default='OBRNAOINICIADA', max_length=20)),
                ('capa', models.ImageField(blank=True, null=True, upload_to='empreendimento/capa/')),
            ],
            options={
                'verbose_name': 'Empreendimento',
                'verbose_name_plural': 'Empreendimentos',
            },
        ),
    ]
