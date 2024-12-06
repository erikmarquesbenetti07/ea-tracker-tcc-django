# Generated by Django 5.1.3 on 2024-11-16 13:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empreendimentos', '0018_empreendimento_visivel'),
        ('usuarios', '0010_usuario_codigo_expiracao_usuario_codigo_verificacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='empreendimento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='usuarios', to='empreendimentos.empreendimento'),
        ),
    ]