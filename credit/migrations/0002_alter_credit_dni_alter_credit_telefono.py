# Generated by Django 4.1.2 on 2022-10-17 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credit',
            name='dni',
            field=models.IntegerField(max_length=20),
        ),
        migrations.AlterField(
            model_name='credit',
            name='telefono',
            field=models.IntegerField(max_length=20),
        ),
    ]