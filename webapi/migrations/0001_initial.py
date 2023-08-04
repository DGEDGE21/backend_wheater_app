# Generated by Django 3.0 on 2023-08-04 15:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('idUsuario', models.BigAutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=50)),
                ('morada', models.CharField(max_length=130)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario_Historico_localizacoes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('localizacao', models.CharField(max_length=130)),
                ('data_de_pesquisa', models.DateField(auto_now_add=True)),
                ('idUsuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='webapi.Usuario')),
            ],
        ),
    ]