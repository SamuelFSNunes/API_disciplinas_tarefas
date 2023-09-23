from django.db import models
from api.models.taskEntity import Task
from api.models.disciplineEntity import Discipline

class TasksDisciplines(models.Model):

  """
    Model to represent the relationship between tasks and disciplines.

    Attributes:
        Tarefa (ForeignKey): A foreign key relationship to the Task model, representing a task associated with a discipline.
        Disciplina (ForeignKey): A foreign key relationship to the Discipline model, representing a discipline associated with a task.
  """
  
  tasks = models.ForeignKey(Task, on_delete=models.CASCADE)
  disciplines = models.ForeignKey(Discipline, on_delete=models.CASCADE)