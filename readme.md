steps

step 1
initiate github
setup virtual env
install django

update and pin dependencies

set up django architecture
todo_list/
│
├── todo_app/
├── todo_project/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── venv/
│
├── manage.py
└── requirements.txt

todo app
todo_app/
│
├── migrations/
│   └── __init__.py
│
├── __init__.py
├── admin.py
├── apps.py
├── models.py
├── tests.py
└── views.py

step 2
configure project
create the url paths and files
in urls.py

run server with command
python manage.py runserver

step 3
design data model

define data models in models.py
### Explanation of Comments:
1. **Imports**:
   - `timezone` is imported from `django.utils` to handle time-related functions.
   - `models` is from `django.db` to define database models.
   - `reverse` is used for generating URLs dynamically based on view names.

2. **`one_week_hence` function**:
   - A helper function that returns the current time plus 7 days. Used as the default value for `due_date` in the `ToDoItem` model.

3. **`ToDoList` Model**:
   - Represents a to-do list, with a `title` that must be unique.
   - `get_absolute_url`: Returns a URL for viewing the to-do list.
   - `__str__`: Displays the list's title in human-readable form.

4. **`ToDoItem` Model**:
   - Represents individual items in a to-do list.
   - Fields include `title`, `description`, `created_date`, `due_date`, and a foreign key to `ToDoList`.
   - `get_absolute_url`: Returns a URL for updating the to-do item.
   - `__str__`: Shows the title and due date for easy identification.
   - `Meta`: The items are ordered by their `due_date` in ascending order.

next create the database with
python manage.py makemigrations todo_app
python manage.py migrate

### Documentation for Database Migration Commands

#### Creating Migrations

```bash
python manage.py makemigrations todo_app
```

- **Description**: This command is used to create migration files for the `todo_app` Django application. Migrations are a way of tracking changes to your models (i.e., database schema) over time.
- **What It Does**: 
  - It analyzes the current state of your models in `todo_app` and compares them to the last migration files. 
  - If any changes (like new models, updated fields, or removed fields) are detected, it generates a new migration file in the `migrations` directory of the `todo_app`.
  - The migration file contains Python code that defines how to apply the changes to the database schema.

#### Applying Migrations

```bash
python manage.py migrate
```

- **Description**: This command applies the migrations to your database. It updates the database schema to match the current state of your models.
- **What It Does**:
  - It looks at all migration files that have not yet been applied and executes them in the order they were created.
  - It updates the database schema accordingly by adding or modifying tables and fields as specified in the migration files.
  - It also creates a special table in the database (usually named `django_migrations`) that keeps track of which migrations have been applied, ensuring that each migration is only run once.

### Summary
- Use `makemigrations` to create new migration files reflecting model changes.
- Use `migrate` to apply these migration files, updating your database schema to align with your Django models.

### Example Workflow
1. Make changes to your models in `todo_app/models.py`.
2. Run `python manage.py makemigrations todo_app` to create the migration files.
3. Run `python manage.py migrate` to apply those changes to your database.

This process ensures that your database structure is always in sync with your Django application’s models, allowing you to effectively manage data storage and retrieval.

### Step 4: Create a To-Do List and Sample To-Do Item

first create super user
python manage.py createsuperuser

import module and register model in admin.py

now you can run
python manage.py runserver
and go to address http://127.0.0.1:8000/admin/
to see the login screen and admin page that displays links to todo lists and todo items




1. **Access the Admin Interface**: 
   - On the left side of the main Django administration page, click on **To do lists**.

2. **Add a New To-Do List**:
   - On the next screen, click the button at the top right that says **ADD TO DO LIST**.
   - In the form that appears, enter a title for your list (e.g., **Things to do today**).
   - Click the **SAVE** button on the extreme right of the screen. 
   - The new list will now appear on a page headed **Select to do list to change**.

3. **Add a Sample To-Do Item**:
   - Instead of selecting the newly created list, click on the **+ Add** button next to **To do items** on the left of the screen.
   - A new form will appear for adding a To-Do item.
   - Fill in the form with the following sample data:
     - **Title**: Start my to-do list
     - **Description**: First things first.
     - **Due Date**: Leave this as it is (it will default to one week from today).
     - **To-Do List**: Select your newly created to-do list title from the dropdown menu.
   - Click the **SAVE** button to save the item.

4. **Explore the Admin Interface**:
   - You have now created one list and one item using the admin interface.
   - Feel free to explore the pages to get a feel for how they work. The admin interface is a useful tool for quickly managing data as a developer but is not intended for regular user access.


step 5 create django views

### Step 5: Update Views for the To-Do List

1. **Open the `views.py` File**:
   - Navigate to the `todo_list/todo_app` directory and open the `views.py` file.

2. **Add the ListView**:
   - Update your `views.py` file with the following code:

next create a base template
Create a new folder inside the todo_app/ directory named templates/. Now add a new file to this folder. You can call it base.html. 


 Create a Base Template

1. **Create a Templates Folder**  
   Inside the `todo_app/` directory, create a new folder named `templates/`. This folder will be used to store all the HTML templates for your Django application.

2. **Add the Base Template**  
   Within the `templates/` folder, create a new file named `base.html`. This file will serve as the foundation for your application's HTML structure and styling.

3. **Structure of `base.html`**  
   Your `base.html` file should include the necessary HTML structure, such as the `<!doctype html>` declaration, `<head>` section for meta tags and stylesheets, and a `<body>` section that will contain a header and a content block. Here's a basic example of what it should look like:

4. **Purpose of the Base Template**  
   The `base.html` file is designed to provide a consistent layout for all pages in your application. By using template inheritance, you can create other templates that extend this base template, allowing you to maintain a uniform look and feel across your site.

Add home page
Django’s convention for the templates belonging to an app is that they live in a folder named templates/<appname> inside the app folder. So although the base template base.html went in the todo_app/templates/ folder, the others will all be placed inside a folder named todo_app/templates/todo_app/:
Your first objective will be to code the template for the home page of your website, traditionally named index.html.
You’ve now created the home page of your application, which will display a list of all your to-do lists if you have any, or an informative message if not. Your user will be directed to other pages, or back to this one, by the URL dispatcher. 


### Step 5: Create a Base Template (Continued)

5. **Add the Home Page Template**  
   To follow Django's convention, create a new folder named `todo_app` inside the `templates/` directory. The structure should be `todo_app/templates/todo_app/`.

   Within this newly created folder, add a file named `index.html`. This file will serve as the template for the home page of your application.



7. **Purpose of the Home Page**  
   The home page will display a list of all the to-do lists that have been created. Each title will be a clickable link that directs users to the corresponding list page. If no to-do lists exist, a friendly message will prompt the user to create one. 


