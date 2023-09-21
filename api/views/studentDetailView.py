from django.forms import ValidationError
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.serializers.studentSerializer import Student, StudentSerializer

class StudentDetailView(APIView):
    """
    API view for detailed operations on a Student instance.

    Attributes:
        None
    """

    def get_object(self, pk):
        """
        Get a Student instance by its primary key.

        Args:
            pk (int): The primary key of the Student.

        Returns:
            Student: The Student instance with the specified primary key.

        Raises:
            Http404: If the Student with the specified primary key does not exist.
        """
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """
        Retrieve a Student instance by its primary key.

        Args:
            request: The HTTP request object.
            pk (int): The primary key of the Student.
            format (str, optional): The format of the response (e.g., JSON).

        Returns:
            Response: A Response object containing the serialized Student instance and a success message.

        Raises:
            Exception: If an error occurs during the retrieval process.
        """
        try:
            instance = self.get_object(pk)
            serializer = StudentSerializer(instance)
            return Response(
                {"detail": "Student Returned Successfully", "object": serializer.data},
                status=status.HTTP_200_OK,
            )
        except Exception as error:
            return Response(
                {
                    "detail": {
                        "error_name": error.__class__.__name__,
                        "error_cause": error.args,
                    }
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    def put(self, request, pk, format=None):
        """
        Update a Student instance by its primary key.

        Args:
            request: The HTTP request object containing the updated data.
            pk (int): The primary key of the Student.
            format (str, optional): The format of the response (e.g., JSON).

        Returns:
            Response: A Response object containing the serialized updated Student instance and a success message.

        Raises:
            ValidationError: If the request body contains no data.
            ValidationError: If the updated data is not valid.
            Exception: If an error occurs during the update process.
        """
        try:
            data = request.data
            if not data:
                raise ValidationError("No data was sent in the request body")
            instance = self.get_object(pk)
            student = StudentSerializer(instance, data=data)
            student.is_valid(raise_exception=True)
            student.save()
            return Response(
                {"detail": "Student successfully changed", "object": student.data},
                status=status.HTTP_201_CREATED,
            )
        except ValidationError as error:
            return Response(
                {
                    "detail": {
                        "error_name": error.__class__.__name__,
                        "error_cause": error.args,
                    }
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        except Exception as error:
            return Response(
                {
                    "detail": {
                        "error_name": error.__class__.__name__,
                        "error_cause": error.args,
                    }
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    def delete(self, request, pk, format=None):
        """
        Delete a Student instance by its primary key.

        Args:
            request: The HTTP request object.
            pk (int): The primary key of the Student.
            format (str, optional): The format of the response (e.g., JSON).

        Returns:
            Response: A Response object containing a success message indicating the deletion.

        Raises:
            Exception: If an error occurs during the deletion process.
        """
        try:
            instance = self.get_object(pk)
            deleted_student = StudentSerializer(instance)
            instance.delete()
            return Response(
                {"detail": "Student deleted successfully", "object": deleted_student.data}
            )
        except Exception as error:
            return Response(
                {
                    "detail": {
                        "error_name": error.__class__.__name__,
                        "error_cause": error.args,
                    }
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
