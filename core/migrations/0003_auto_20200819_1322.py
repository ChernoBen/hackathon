# Generated by Django 3.1 on 2020-08-19 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200819_1318'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empresa',
            name='estado',
        ),
        migrations.AddField(
            model_name='empresa',
            name='estado',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='core.estados'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='estados',
            name='sigla',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
