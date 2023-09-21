from django.forms import ValidationError
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.serializers.disciplinesSerializer import Discipline, DisciplineSerializer

class DisciplineDetailView(APIView):

  """
    API view for detailed operations on a Discipline instance.

    Attributes:
        None
  """

  def get_object(self, pk):

    """
        Get a Discipline instance by its primary key.

        Args:
            pk (int): The primary key of the Discipline.

        Returns:
            Discipline: The Discipline instance with the specified primary key.

        Raises:
            Http404: If the Discipline with the specified primary key does not exist.
    """
    
    try:

      """
        Retrieve a Discipline instance by its primary key.

        Args:
            request: The HTTP request object.
            pk (int): The primary key of the Discipline.
            format (str, optional): The format of the response (e.g., JSON).

        Returns:
            Response: A Response object containing the serialized Discipline instance and a success message.

        Raises:
            Exception: If an error occurs during the retrieval process.
        """
      
      return Discipline.objects.get(pk=pk)
    except Discipline.DoesNotExist:
      raise Http404
  def get(self, request, pk, format=None):

    """
        Update a Discipline instance by its primary key.

        Args:
            request: The HTTP request object containing the updated data.
            pk (int): The primary key of the Discipline.
            format (str, optional): The format of the response (e.g., JSON).

        Returns:
            Response: A Response object containing the serialized updated Discipline instance and a success message.

        Raises:
            ValidationError: If the request body contains no data.
            ValidationError: If the updated data is not valid.
            Exception: If an error occurs during the update process.
    """

    try:
      instace = self.get_object(pk)
      disciplines = DisciplineSerializer(instace)
      return Response({"detail": "Disciplines Returned Successfully",
                        "object": disciplines.data}, status=status.HTTP_200_OK)
    except Exception as error:
      return Response({"detail": { 'error_name': error.__class__.__name__, 'error_cause': error.args}}
                      , status=status.HTTP_500_INTERNAL_SERVER_ERROR)


  def put(self, request, pk, format=None):

    """
        Delete a Discipline instance by its primary key.

        Args:
            request: The HTTP request object.
            pk (int): The primary key of the Discipline.
            format (str, optional): The format of the response (e.g., JSON).

        Returns:
            Response: A Response object containing a success message indicating the deletion.

        Raises:
            Exception: If an error occurs during the deletion process.
    """
    
    try:
      data = request.data
      if not data:
        raise ValidationError("no data was sent in the request body")
      instace = self.get_object(pk)
      disciplines = DisciplineSerializer(instace, data=data)
      disciplines.is_valid(raise_exception=True)
      disciplines.save()
      return Response({"detail": "Disciplines successfully changed", "object": disciplines.data}
                      , status=status.HTTP_201_CREATED)
    except ValidationError as error:
      return Response({"detail": { 'error_name': error.__class__.__name__, 'error_cause': error.args}}
                      , status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as error:
      return Response({"detail": { 'error_name': error.__class__.__name__, 'error_cause': error.args}}
                      , status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
  def delete(self, request, pk, format=None):
    try:

      instace = self.get_object(pk)
      deleted_disciplines = DisciplineSerializer(instace)
      instace.delete()
      return Response({"detail": "Disciplines deleted successfully", "object": deleted_disciplines.data})
    except Exception as error:
      return Response({"detail": { 'error_name': error.__class__.__name__, 'error_cause': error.args}}
                      , status=status.HTTP_500_INTERNAL_SERVER_ERROR)
