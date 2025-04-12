# Generated by Django 5.1.7 on 2025-04-09 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('risks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='riskevaluation',
            name='estado',
            field=models.CharField(choices=[('pendiente', 'Pendiente'), ('revision', 'En revisión'), ('mitigado', 'Mitigado')], default='pendiente', max_length=20),
        ),
    ]
