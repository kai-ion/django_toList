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

### New Views

To enable the creation and update of to-do lists and items, you'll need to update your templates with links that trigger the new views.

1. **Adding a Button to Create a New List (index.html):**
   Just before the `{% endblock %}` tag in `index.html`, add a button that, when clicked, will send a request matching the "list-add" URL pattern. The "list-add" route, defined in `todo_app/urls.py`, will generate a URL that looks like "list/add/" and will instantiate the `ListCreate` view to allow users to create a new list.

2. **Updating Onclick Events in todo_list.html:**
   In `todo_list.html`, replace the dummy `onclick` events with event handlers that invoke the new URLs for updating and adding items. 

   - For updating items, the URL named "item-update" requires two parameters: the `list_id` and the `item_id`.
   - For adding new items, the "item-add" URL requires only the `todo_list.id` as a parameter.

   These URLs will be constructed dynamically using the `{% url %}` tag, which combines the URL pattern name with context variables to generate appropriate hyperlinks. For example, in lines 15 to 21, you're using an `onclick` event handler to trigger a button-like div that directs to the "item-update" view for an existing item.

3. **Creating Templates for ListCreate, ItemCreate, and ItemUpdate Views:**
   You will need templates to render the forms for creating and updating both ToDoLists and ToDoItems.

   - **todolist_form.html:**
     This template will handle the form for creating a new list. Inside this template, you'll include a `<form>` element that generates a POST request when submitted. The form will only contain the title of the list, and you will utilize the `{{ form.as_p }}` tag to auto-generate the form content based on the model's structure.
     
     The `{{ form.as_p }}` tag will render the form fields inside a `<p>` tag, making it easy to layout the form with minimal effort. Don't forget to include the `{% csrf_token %}` for security purposes.

   - **todoitem_form.html:**
     This template is similar but handles the creation or update of individual to-do items. Since a to-do item has multiple fields, you’ll render the form as a table for better structure using `{{ form.as_table }}`. When submitted, the form generates a POST request to create or update the item. A "Cancel" button will redirect the user back to the "list" URL with the current list ID as a parameter.

4. **Testing Your Application:**
   Run your development server to verify that you can now create new to-do lists, add items to those lists, and update existing items. Check the form submissions, ensuring that the POST requests are processed correctly and that users are redirected appropriately after creating or updating their lists or items.

```bash
python manage.py runserver
```

### Step 7: Delete To-Do Lists and Items

To allow users to delete both To-Do Lists and To-Do Items, you'll need to implement the delete functionality by creating two new views that subclass `DeleteView` from Django's class-based views. These views will handle the deletion process and redirect the user to the appropriate page after the deletion.

First, ensure that you import the necessary modules from `django.views.generic`, such as `DeleteView`, in your `views.py` file.

Next, create two separate view classes:
1. **ListDelete** – This will manage the deletion of an entire To-Do List. Once a list is deleted, the user will be redirected to the homepage or another list-related page.
2. **ItemDelete** – This will handle the deletion of a single To-Do Item from a list. After the deletion, the user will be redirected back to the associated To-Do List to view the remaining items.

These views will ensure that users can efficiently remove lists or individual items, streamlining their interaction with the To-Do List application.


To add deletion functionality to the To-Do List and To-Do Item objects, follow these steps:

1. **Create Deletion Templates**:
   - Create a new template named `todolist_confirm_delete.html` for confirming the deletion of a `ToDoList` object.
   - Create another template named `todoitem_confirm_delete.html` for confirming the deletion of a `ToDoItem` object.
   - Both templates should include a confirmation message and two buttons: one for confirming the deletion and one for canceling the action.
   - If the user confirms the deletion, the object is deleted, and Django redirects to the appropriate page. For `ToDoList` objects, the redirection will be to the home page. For `ToDoItem` objects, the redirection will be to the parent list page.

2. **Define Routes for Deletion**:
   - In the `urls.py` file, define the routes for deleting `ToDoList` and `ToDoItem` objects.
   - Ensure that the appropriate URLs are mapped to the `DeleteView` subclasses responsible for handling the deletion logic.

3. **Cancellation Behavior**:
   - For `ToDoList` deletion, if the user cancels the action, they are redirected to the home page.
   - For `ToDoItem` deletion, if the user cancels the action, they are redirected to the parent list view.

This ensures that users can delete both to-do lists and items with confirmation prompts, improving the overall functionality and user experience.



To enable deletion functionality within the user interface, follow these steps:

1. **Add a Delete Button for To-Do Items**:
   - Modify the `todoitem_form.html` template to include a button that allows users to delete the current `ToDoItem`.
   - This button should link to the corresponding deletion URL, enabling users to remove an item from the to-do list.

2. **Add a Delete Button for To-Do Lists**:
   - Similarly, in the `todolist.html` template, add a button that allows users to delete an entire `ToDoList`.
   - This button should link to the deletion URL for the specific list, giving users the option to remove a list along with its associated items.

By incorporating these buttons into the templates, you provide users with the ability to directly delete items and lists from the interface, making the application more interactive and functional.