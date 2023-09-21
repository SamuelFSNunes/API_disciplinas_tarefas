from rest_framework import serializers
from api.models.disciplineEntity import Discipline

class DisciplineSerializer(serializers.ModelSerializer):
  """
    Serializer for the Discipline model.

    This serializer is used to convert Discipline model instances into JSON representation and vice versa.

    Attributes:
        Meta (class): A class defining metadata options for the serializer.
            - model (Discipline): The Django model to be serialized.
            - fields (str): A special value "__all__" indicates that all fields in the model should be included in the serialization.
  """
  class Meta:
    """
        Metadata options for the DisciplineSerializer.

        Attributes:
            model (Discipline): The Django model to be serialized.
            fields (str): A special value "__all__" indicates that all fields in the model should be included in the serialization.
    """
    model = Discipline
    fields = "__all__"