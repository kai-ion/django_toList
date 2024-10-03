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