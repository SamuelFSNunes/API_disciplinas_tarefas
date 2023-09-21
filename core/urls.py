from django.contrib import admin
from django.urls import path
from api.views.studentView import StudentView
from api.views.studentDetailView import StudentDetailView
from api.views.taskView import TaskView
from api.views.taskDetailView import TaskDetailView
from api.views.disciplineView import DisciplineView
from api.views.disciplineDetailView import DisciplineDetailView
from api.views.taskAlunosView import TasksStudentsView

urlpatterns = [
    path('admin/', admin.site.urls),  # URL for Django admin site.

    # URLs for Student API views
    path('api/alunos/', StudentView.as_view()),  # List and create students
    path('api/alunos/<int:pk>/', StudentDetailView.as_view()),  # Retrieve, update, or delete a specific student

    # URLs for Task API views
    path('api/tarefas/', TaskView.as_view()),  # List and create tasks
    path('api/tarefas/<int:pk>/', TaskDetailView.as_view()),  # Retrieve, update, or delete a specific task

    # URLs for Discipline API views
    path('api/disciplinas/', DisciplineView.as_view()),  # List and create disciplines
    path('api/disciplinas/<int:pk>/', DisciplineDetailView.as_view()),  # Retrieve, update, or delete a specific discipline

    # URL for retrieving tasks associated with a specific student
    path('api/alunos/<int:pk>/tarefas/', TasksStudentsView.as_view())
]
