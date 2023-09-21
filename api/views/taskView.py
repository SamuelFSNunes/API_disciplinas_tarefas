from django.forms import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.serializers.taskSerializer import Task, TaskSerializer

class TaskView(APIView):
    """
    API view for performing CRUD operations on Task instances.

    Attributes:
        None
    """

    def get(self, request, format=None):
        """
        Retrieve a list of all Task instances.

        Args:
            request: The HTTP request object.
            format (str, optional): The format of the response (e.g., JSON).

        Returns:
            Response: A Response object containing a list of serialized Task instances or a message indicating no records found.

        Raises:
            Exception: If an error occurs during the retrieval process.
        """
        try:
            instances = Task.objects.all()
            task_serializer = TaskSerializer(instances, many=True)
            if not task_serializer.data:
                return Response({
                    "detail": "There are no tasks registered in the system",
                    "object": task_serializer.data
                }, status=status.HTTP_200_OK)
            return Response({
                "detail": "Tasks Returned Successfully",
                "object": task_serializer.data
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
        Create a new Task instance.

        Args:
            request: The HTTP request object containing the data for the new Task.
            format (str, optional): The format of the response (e.g., JSON).

        Returns:
            Response: A Response object containing the serialized created Task instance and a success message.

        Raises:
            ValidationError: If the request body contains no data.
            ValidationError: If the submitted data is not valid.
            Exception: If an error occurs during the creation process.
        """
        try:
            data = request.data
            if not data:
                raise ValidationError("No data was sent in the request body")
            task_serializer = TaskSerializer(data=data)
            task_serializer.is_valid(raise_exception=True)
            task_serializer.save()
            return Response({
                "detail": "Tasks created successfully",
                "object": task_serializer.data
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
