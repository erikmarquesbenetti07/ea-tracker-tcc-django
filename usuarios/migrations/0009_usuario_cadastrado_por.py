# Generated by Django 5.1.1 on 2024-11-06 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0008_rename_quadra_usuario_unidade'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='cadastrado_por',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
