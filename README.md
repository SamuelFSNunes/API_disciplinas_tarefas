# API_DISCIPLINAS_TAREFAS

To get started with this application, you need to follow the steps below and have Python installed on your computer.

# Installing Python
Visit the website https://www.python.org/downloads/ and install it according to your operating system (Windows, Linux, Mac).

# Enabling script execution
For Windows: https://cursos.alura.com.br/forum/topico-execucao-de-script-desativada-219081

# Create and activate a virtual environment
Execute the following commands:

python -m venv .env
.env\Scripts\activate

With the virtual environment created and activated, we can proceed with the installation of the requirements.

# Installing requirements

Execute the following command:

pip install -r requirements.txt

This will install all the necessary technologies to run this application.

# Almost there, just one more command

Now, simply enter the following command, and your API will be up and running!

python manage.py runserver

# Now, to view and test the application, access the following URLs

Legend:
int:pk - Refers to the ID number

#   URLs for Students API views
URL ('api/alunos/')
URL ('api/alunos/int:pk/')

# URLs for Task API views
URL ('api/tarefas/')
URL ('api/tarefas/int:pk/')

# URLs for Discipline API views
URL ('api/disciplinas/')
URL ('api/disciplinas/int:pk/')

# URL for retrieving tasks associated with a specific student
path('api/alunos/int:pk/tarefas/')

# To make it easier to interact with the API, I've provided a POSTMAN collection

First, install Postman, follow the link: https://www.postman.com/downloads/
Open the application and click on "import"
Select the file API TEST.postman_collection.json

Now, send the pre-defined requests.