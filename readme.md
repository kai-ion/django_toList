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


next build a request handler
You’ve already created the app-level URL file. Now it’s time to add the first route to that file. Edit the file todo_app/urls.py to add the route

next add a subclass Listview to display a list of todo items
Now you can do something very similar to display a list of to-do items. You’ll start by creating another view class, this time called ItemListView. Like the class ListListView, ItemListView will extend the generic Django class ListView. Open views.py and add your new class

Show the Items in a To-Do List
Your next task is to create a template for displaying the TodoItems in a given list. Once again, the {% for <item> in <list> %} … {% endfor %} construct will be indispensable. Create the new template, todo_list.html

So you’ve coded an ItemListView class, but so far, there’s no way for your user to invoke it. You need to add a new route into urls.py so that ItemListView can be used

## Step 6: Create and Update Model Objects in Django

In this step, we will focus on adding new views that support **Create** and **Update** actions for the To-Do application. Afterward, URLs will be added to reference these views, and the `todo_items.html` template will be updated to allow users to navigate to these new URLs for creating and updating items in their to-do list.

### ListCreate View

The `ListCreate` view is responsible for creating a new to-do list. It defines a form with a single field, the **title** of the list, which is the only public attribute of a `ToDoList` object. In addition to this, the form itself has a title, which is passed in the context data. This title helps guide the user by indicating that they are creating a new list, enhancing the user experience.

### ItemCreate View

The `ItemCreate` view generates a form with four fields: the to-do list the item belongs to, the title of the item, a description, and a due date. Two methods are overridden to enhance the functionality of the form:

- **`get_initial()`**: This method pre-populates the form with useful initial data, such as automatically selecting the correct to-do list based on the list ID passed in the URL.
- **`get_context_data()`**: This method adds additional context for the template, such as the specific to-do list the item is being added to, as well as a custom title for the form ("Create a new item").
- **`get_success_url()`**: This method defines the URL the user is redirected to after successfully creating a new item. In this case, it redirects to the list view, where the user can see the entire to-do list that now includes the newly created item.

### ItemUpdate View

The `ItemUpdate` view is almost identical to `ItemCreate`, but it is used for updating existing to-do items rather than creating new ones. It also supplies a more appropriate title in the form, such as "Edit item", to let the user know they are updating an existing item. Like `ItemCreate`, it uses the same fields (to-do list, title, description, due date) and includes custom context and success URL behavior. The key difference lies in the form title, which clearly communicates to the user that they are editing an item rather than creating one. 

By defining these views, users can now create and update both to-do lists and items, making the application more dynamic and user-friendly.


In this step, you'll define routes that allow users to access the new views for creating and updating to-do lists and items. The routes will be added to the `urlpatterns` array, each with a unique name to allow for easy reference in your templates and views.

- The "list-add" route will allow users to add a new to-do list. This route points to the view responsible for creating new lists, and it doesn't require any dynamic parameters.
- The "item-add" route will enable users to add a new item to a specific to-do list. This route takes a dynamic `list_id` parameter, which ensures that the new item is associated with the correct list.
- The "item-update" route is for updating an existing item within a to-do list. This route takes two dynamic parameters: `list_id` to identify the to-do list and `pk` (primary key) to identify the specific item being updated.

By adding these routes, you'll ensure that users can navigate to the appropriate pages for creating and updating lists and items, with the necessary data values already set based on the URL parameters. These routes will be named "list-add", "item-add", and "item-update" for easy reference throughout the application.

New Views
Next, you’ll need to provide some links in your templates to activate the new views. Just before the {% endblock %} tag in index.html, add a button
A click on this button will now generate a request with the "list-add" pattern. If you look back at the corresponding urlpattern item in todo_app/urls.py, then you’ll see that the associated URL looks like "list/add/", and it causes the URL dispatcher to instantiate a ListCreate view.

Now you’ll update the two dummy onclick events in todo_list.html

The onclick event handlers now invoke the new URLs named "item-update" and "item-add". Notice again the syntax {% url "key" [param1 [, param2 [,...]]]%} in lines 18 and 32, where the urlpattern name is combined with data from context to construct hyperlinks.

For example, in lines 15 to 21, you’re setting up a button-like div element with an onclick event handler.

Notice that the "item-update" URL requires IDs for both the list and the item to be updated, whereas "item-add" required only todo_list.id.

You’ll need templates to render your new ListCreate, ItemCreate, and ItemUpdate views. The first one that you’ll tackle is the form for creating a new list. Create a new template file named todolist_form.html

This page contains a <form> element in lines 9 to 19 that’ll generate a POST request when the user submits it, with the user-updated form contents as part of its payload. In this case, the form contains only the list title.

Line 10 uses the {% csrf_token %} macro, which generates a Cross-Site Request Forgery token, a necessary precaution for modern web forms.

Line 11 uses the {{ form.as_p }} tag to invoke the view class’s .as_p() method. This auto-generates the form contents from the fields attribute and the model structure. The form will be rendered as HTML inside a <p> tag.

Next, you’ll create another form that’ll allow the user to create a new ToDoItem, or edit the details of an existing one. Add the new template todoitem_form.html
This time, you’re rendering the form as a table (lines 9 to 11), because there are several fields per item. Both CreateView and UpdateView contain a .form member with convenient methods like form.as_p() and form.as_table() to perform an automatic layout. The Submit button will generate a POST request using the form’s contents. The Cancel button will redirect the user to the "list" URL, passing along the current list id as a parameter.

Run your development server again to verify that you can now create new lists and add items to those lists