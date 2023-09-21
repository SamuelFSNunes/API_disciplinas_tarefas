from django.db import models


class Discipline(models.Model):
  """
    Model to represent a discipline.

    Attributes:
        name (CharField): The name of the discipline.
        description (TextField): An optional description of the discipline.

    Methods:
        __str__(): Returns a string representation of the discipline, using its name.
    """
  
  name = models.CharField(max_length=200, null=False, blank=False)
  description = models.TextField(null=True, blank=True)

  def __str__(self) -> str:

    """
        Returns a string representation of the discipline, using its name.

        Returns:
            str: A string representing the name of the discipline.
        """
    
    return self.name