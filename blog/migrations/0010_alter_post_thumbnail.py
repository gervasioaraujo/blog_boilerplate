# Generated by Django 3.2 on 2021-04-07 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20210407_2333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='uploads', verbose_name='imagem destacada'),
        ),
    ]
