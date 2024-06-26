# Generated by Django 5.0.4 on 2024-04-24 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppUsuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=100, unique=True, verbose_name='Nombre Usuario')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='E-mail')),
                ('telefono', models.CharField(blank=True, max_length=150, null=True, verbose_name='Telefono')),
            ],
        ),
    ]
