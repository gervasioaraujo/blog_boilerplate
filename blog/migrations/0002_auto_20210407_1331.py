# Generated by Django 3.2 on 2021-04-07 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='updated_at',
            field=models.DateField(auto_now=True, null=True, verbose_name='Atualizado em'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Criado em'),
        ),
    ]