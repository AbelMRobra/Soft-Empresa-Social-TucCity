# Generated by Django 3.2.3 on 2021-06-15 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0009_clientes_otros_datos'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientes',
            name='password',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='password'),
        ),
    ]