# Generated by Django 4.2.5 on 2023-09-21 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_tarefa_disciplinas'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarefa',
            name='disciplinas',
            field=models.ManyToManyField(blank=True, to='api.disciplina'),
        ),
    ]
