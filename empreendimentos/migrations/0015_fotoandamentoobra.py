# Generated by Django 5.1.1 on 2024-10-11 12:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empreendimentos', '0014_remove_empreendimento_quantidade_quadras_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FotoAndamentoObra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mes', models.CharField(max_length=20)),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='empreendimento/obra/')),
                ('empreendimento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empreendimentos.empreendimento', verbose_name='Empreendimento')),
            ],
            options={
                'verbose_name': 'Foto Andamento Obra',
                'verbose_name_plural': 'Fotos Andamento Obras',
            },
        ),
    ]
