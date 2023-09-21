# API_disciplinas_tarefas

Running the Django Code
Step 1: Clone the Repository
Clone your Django project repository from the source where it's hosted. If it's on GitHub, you can use the following command:

git clone <repository_url>
Replace <repository_url> with the actual URL of your Git repository.

Step 2: Navigate to the Project Directory
Change your current directory to the project directory:

cd <project_directory>
Replace <project_directory> with the name of your Django project directory.

Step 3: Create a Virtual Environment (Optional, but Recommended)
It's a good practice to create a virtual environment to isolate your project dependencies. To create a virtual environment, run:

python -m venv venv
Activate the virtual environment:

On Windows:

venv\Scripts\activate
On macOS and Linux:

source venv/bin/activate
Step 4: Install Dependencies
Install the project dependencies listed in your requirements.txt file using pip:

pip install -r requirements.txt
Step 5: Set Up the Database
You need to apply database migrations to create the database schema:

python manage.py migrate
Step 6: Create a Superuser (Admin)
If your project has an admin panel, create a superuser to access it:

python manage.py createsuperuser
Follow the prompts to set a username, email, and password.

Step 7: Run the Development Server
Start the Django development server:

python manage.py runserver
The server will start, and you'll see output similar to:

Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
Step 8: Access the Application
Open a web browser and go to http://127.0.0.1:8000/ to access your Django application.

Step 9: Access the Admin Panel
If you created a superuser in Step 6, you can access the admin panel by going to http://127.0.0.1:8000/admin/. Log in with the superuser credentials you created.

Step 10: Explore and Test
Explore your Django application, test its features, and interact with the API endpoints you've defined in your code.

You have successfully set up and run your Django project!

Additional Notes
Remember to deactivate the virtual environment (if you created one) when you're done working on your project. You can do this by running deactivate in the terminal.
Make sure to keep your Django project and its dependencies updated regularly.
Refer to the specific documentation of your project for any additional setup or configuration steps that may be required.
Enjoy working on your Django project!