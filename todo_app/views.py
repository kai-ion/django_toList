# todo_list/todo_app/views.py

# Import necessary modules for rendering views and using generic class-based views
from django.shortcuts import render
from django.views.generic import ListView  # Import ListView for creating list-based views
from .models import ToDoList, ToDoItem  # Import ToDoList and ToDoItem models

# Define a view for displaying a list of To-Do Lists
class ListListView(ListView):
    model = ToDoList  # Specify the model to use for this view
    template_name = "todo_app/index.html"  # Specify the template to render

# Define a view for displaying items within a specific To-Do List
class ItemListView(ListView):
    model = ToDoItem  # Specify the model to use for this view
    template_name = "todo_app/todo_list.html"  # Specify the template to render

    # Override the get_queryset method to filter To-Do Items by the selected list
    def get_queryset(self):
        # Return ToDoItem objects filtered by the todo_list_id passed in the URL
        return ToDoItem.objects.filter(todo_list_id=self.kwargs["list_id"])

    # Override the get_context_data method to include additional context for the template
    def get_context_data(self, **kwargs):
        # Get the existing context data
        context = super().get_context_data(**kwargs)
        # Add the specific ToDoList object to the context using the list_id from the URL
        context["todo_list"] = ToDoList.objects.get(id=self.kwargs["list_id"])
        return context  # Return the updated context
