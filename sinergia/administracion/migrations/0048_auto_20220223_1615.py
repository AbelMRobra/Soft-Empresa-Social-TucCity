# Generated by Django 3.2.3 on 2022-02-23 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0047_auto_20220222_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='proveedor',
            name='banco',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Banco'),
        ),
        migrations.AddField(
            model_name='proveedor',
            name='cbu',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='CBU'),
        ),
        migrations.AddField(
            model_name='proveedor',
            name='n_cuenta',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Nº cuenta'),
        ),
    ]