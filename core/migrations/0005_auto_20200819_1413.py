# Generated by Django 3.1 on 2020-08-19 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20200819_1406'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cadastro',
            name='estado',
        ),
        migrations.AddField(
            model_name='cadastro',
            name='estado',
            field=models.ManyToManyField(to='core.Estados'),
        ),
        migrations.RemoveField(
            model_name='cadastro',
            name='tipo',
        ),
        migrations.AddField(
            model_name='cadastro',
            name='tipo',
            field=models.ManyToManyField(to='core.Categoria'),
        ),
    ]