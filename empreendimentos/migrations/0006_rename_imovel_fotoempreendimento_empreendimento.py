# Generated by Django 5.1.1 on 2024-09-16 21:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empreendimentos', '0005_alter_empreendimento_estado_fotoempreendimento'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fotoempreendimento',
            old_name='imovel',
            new_name='empreendimento',
        ),
    ]
