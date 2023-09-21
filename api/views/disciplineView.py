from django.forms import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.serializers.disciplinesSerializer import Discipline, DisciplineSerializer

class DisciplineView(APIView):
    """
    API view for performing CRUD operations on Discipline instances.

    Attributes:
        None
    """

    def get(self, request, format=None):
        """
        Retrieve a list of all Discipline instances.

        Args:
            request: The HTTP request object.
            format (str, optional): The format of the response (e.g., JSON).

        Returns:
            Response: A Response object containing a list of serialized Discipline instances or a message indicating no records found.

        Raises:
            Exception: If an error occurs during the retrieval process.
        """
        try:
            instances = Discipline.objects.all()
            discipline_serializer = DisciplineSerializer(instances, many=True)
            if not discipline_serializer.data:
                return Response({
                    "detail": "There are no disciplines registered in the system",
                    "object": discipline_serializer.data
                }, status=status.HTTP_200_OK)
            return Response({
                "detail": "Disciplines Returned Successfully",
                "object": discipline_serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as error:
            return Response({
                "detail": {
                    'error_name': error.__class__.__name__,
                    'error_cause': error.args
                }
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request, format=None):
        """
        Create a new Discipline instance.

        Args:
            request: The HTTP request object containing the data for the new Discipline.
            format (str, optional): The format of the response (e.g., JSON).

        Returns:
            Response: A Response object containing the serialized created Discipline instance and a success message.

        Raises:
            ValidationError: If the request body contains no data.
            ValidationError: If the submitted data is not valid.
            Exception: If an error occurs during the creation process.
        """
        try:
            data = request.data
            if not data:
                raise ValidationError("No data was sent in the request body")
            discipline_serializer = DisciplineSerializer(data=data)
            discipline_serializer.is_valid(raise_exception=True)
            discipline_serializer.save()
            return Response({
                "detail": "Disciplines created successfully",
                "object": discipline_serializer.data
            }, status=status.HTTP_201_CREATED)
        except ValidationError as error:
            return Response({
                "detail": {
                    'error_name': error.__class__.__name__,
                    'error_cause': error.args
                }
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as error:
            return Response({
                "detail": {
                    'error_name': error.__class__.__name__,
                    'error_cause': error.args
                }
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
