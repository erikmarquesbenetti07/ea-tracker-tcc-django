# Generated by Django 5.1.1 on 2024-10-11 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empreendimentos', '0013_empreendimento_quantidade_blocos_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empreendimento',
            name='quantidade_quadras',
        ),
        migrations.AlterField(
            model_name='empreendimento',
            name='quantidade_blocos',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
