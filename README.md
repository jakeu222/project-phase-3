CLI To-Do App Readme
This is a command-line interface to-do list application thathas a user and task table connected with a one to many relationship that are uploaded to the todo.db database. The code is implemented in Python using SQLAlchemy and Inquirer. The CLI allows users to interact with their to-do list through text-based commands. Below, you'll find a brief guide on how to set up and operate the CLI. 

Setting Up and Running the Application
To set up and run the CLI To-Do App, follow these steps:

Install pipenv: If you don't have pipenv installed, you can do so using pip, the Python package manager:

(pip install pipenv)

Navigate to the App Directory: Using your terminal or command prompt, navigate to the directory where the CLI To-Do App code is located.

Install Dependencies: Inside the project directory, run the following command to create a virtual environment and install the necessary dependencies:

(pipenv install)

Activate the Virtual Environment: To activate the virtual environment, run:

(pipenv shell)

Run the CLI: With the virtual environment active, run the CLI script:

(python cli.py)

How to Operate
Once the CLI is running, you can use the following commands:

Create a User Profile: Enter your username to check if a profile exists. If not, you can create a new one.

Add a Task: Add a new task description to your user profile.

Display Tasks: View your tasks and choose which one to update or delete.

Mark a Task as Completed: Indicate whether a task is completed by typing "yes" or "no."

Delete a Completed Task: Delete a completed task if you no longer need it.


Follow the prompts and commands to manage your to-do list efficiently. Enjoy using the CLI To-Do App!