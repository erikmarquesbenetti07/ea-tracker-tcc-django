# Generated by Django 5.1.1 on 2024-09-18 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empreendimentos', '0007_documentoempreendimento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentoempreendimento',
            name='arquivo',
            field=models.FileField(blank=True, null=True, upload_to='empreendimento/documento/'),
        ),
    ]