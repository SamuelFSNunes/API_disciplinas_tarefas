from rest_framework import serializers
from api.models.studentEntity import Student

class StudentSerializer(serializers.ModelSerializer):
  """
    Serializer for the Student model.

    This serializer is used to convert Student model instances into JSON representation and vice versa.

    Attributes:
        Meta (class): A class defining metadata options for the serializer.
            - model (Student): The Django model to be serialized.
            - fields (str): A special value "__all__" indicates that all fields in the model should be included in the serialization.
  """
  class Meta:
    """
        Metadata options for the StudentSerializer.

        Attributes:
            model (Student): The Django model to be serialized.
            fields (str): A special value "__all__" indicates that all fields in the model should be included in the serialization.
    """
    model = Student
    fields = "__all__"