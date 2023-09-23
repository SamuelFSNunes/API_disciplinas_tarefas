from django.forms import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.serializers.taskSerializer import Task, TaskSerializer

class TasksStudentsView(APIView):
    """
    API view for retrieving tasks associated with a specific student.

    Attributes:
        None
    """

    def get(self, request, pk, format=None):
        """
        Retrieve tasks associated with a specific student.

        Args:
            request: The HTTP request object.
            pk (int): The primary key of the student.
            format (str, optional): The format of the response (e.g., JSON).

        Returns:
            Response: A Response object containing a list of serialized Task instances associated with the student.

        Raises:
            Task.DoesNotExist: If no tasks are found for the specified student.
            Exception: If an error occurs during the retrieval process.
        """
        try:
            tasks = Task.objects.filter(student=pk)
            serializer = TaskSerializer(tasks, many=True)
            return Response(serializer.data)
        except Task.DoesNotExist as error:
            return Response({
                "detail": {
                    'error_name': error.__class__.__name__,
                    'error_cause': error.args
                }
            }, status=status.HTTP_404_NOT_FOUND)
        except Exception as error:
            return Response({
                "detail": {
                    'error_name': error.__class__.__name__,
                    'error_cause': error.args
                }
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
