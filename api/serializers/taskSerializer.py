from rest_framework import serializers
from api.models.taskEntity import Task

class TaskSerializer(serializers.ModelSerializer):

  """
    Serializer for the Task model.

    This serializer is used to convert Task model instances into JSON representation and vice versa.

    Attributes:
        Meta (class): A class defining metadata options for the serializer.
            - model (Task): The Django model to be serialized.
            - fields (str): A special value "__all__" indicates that all fields in the model should be included in the serialization.
  """
  
  class Meta:

    """
        Metadata options for the TaskSerializer.

        Attributes:
            model (Task): The Django model to be serialized.
            fields (str): A special value "__all__" indicates that all fields in the model should be included in the serialization.
    """
    
    model = Task
    fields = "__all__"