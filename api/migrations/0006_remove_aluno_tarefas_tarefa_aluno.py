# Generated by Django 4.2.5 on 2023-09-21 01:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_remove_tarefa_aluno_aluno_tarefas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aluno',
            name='tarefas',
        ),
        migrations.AddField(
            model_name='tarefa',
            name='aluno',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.aluno'),
            preserve_default=False,
        ),
    ]