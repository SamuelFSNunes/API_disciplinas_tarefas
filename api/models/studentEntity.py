from django.db import models

class Student(models.Model):

  """
    Model to represent a student.

    Attributes:
        name (CharField): The name of the student.
        email (EmailField): The email address of the student, must be unique.

    Methods:
        __str__(): Returns a string representation of the student, using their name.
    """
  
  name = models.CharField(max_length=200, null=False, blank=False)
  email = models.EmailField(max_length=254, null=False, blank=False, unique=True)

  def __str__(self) -> str:
    
    """
        Returns a string representation of the student, using their name.

        Returns:
            str: A string representing the name of the student.
        """
    
    return self.nome