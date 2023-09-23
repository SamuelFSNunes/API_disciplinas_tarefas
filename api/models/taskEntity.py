from django.db import models
from api.models.studentEntity import Student
from api.models.disciplineEntity import Discipline

class Task(models.Model):

  """
    Model to represent a task.

    Attributes:
        title (CharField): The title of the task.
        description (TextField): An optional description of the task.
        delivery_date (DateField): The delivery date of the task.
        completed (BooleanField): A flag indicating whether the task is completed or not.
        aluno (ForeignKey): A foreign key relationship to the Student model, representing the student associated with the task.
        disciplinas (ManyToManyField): A many-to-many relationship to the Discipline model, representing the disciplines associated with the task.

    Methods:
        __str__(): Returns a string representation of the task, using its title.
    """
  
  title = models.CharField(max_length=200, null=False, blank=False)
  description = models.TextField(null=True, blank=True)
  delivery_date = models.DateField()
  completed = models.BooleanField(null=True, blank=True, default=False)
  student = models.ForeignKey(Student, on_delete=models.CASCADE)
  discipline = models.ManyToManyField(Discipline, blank=True)

  def __str__(self) -> str:

    """
        Returns a string representation of the task, using its title.

        Returns:
            str: A string representing the title of the task.
    """
    
    return self.title
  
  