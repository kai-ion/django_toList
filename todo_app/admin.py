# todo_list/todo_app/admin.py

# Import the necessary modules from Django
from django.contrib import admin  # Allows us to register models with the Django admin interface
from todo_app.models import ToDoItem, ToDoList  # Importing the models to be registered

# Register the ToDoItem model with the admin site
admin.site.register(ToDoItem)  # This makes the ToDoItem model accessible in the admin panel

# Register the ToDoList model with the admin site
admin.site.register(ToDoList)  # This makes the ToDoList model accessible in the admin panel
