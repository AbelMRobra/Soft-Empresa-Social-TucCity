# Generated by Django 3.2.3 on 2021-10-18 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0028_auto_20211018_1952'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagos',
            name='comentarios',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Comentarios'),
        ),
    ]