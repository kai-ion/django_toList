# todo_list/todo_app/views.py

# Import necessary modules for rendering views and using generic class-based views
from django.shortcuts import render
from django.views.generic import ListView  # Import ListView for creating list-based views
from .models import ToDoList, ToDoItem  # Import ToDoList and ToDoItem models
from django.urls import reverse, reverse_lazy  # reverse and reverse_lazy for generating URLs in views
from django.views.generic import (  # Importing generic views to handle CRUD operations
    ListView,   # Used for displaying lists of objects
    CreateView, # Used for creating new objects
    UpdateView, # Used for updating existing objects
    DeleteView, # Used for deleting objects
)

# Define a view for displaying a list of To-Do Lists
class ListListView(ListView):
    model = ToDoList  # Specify the model to use for this view (ToDoList)
    template_name = "todo_app/index.html"  # Specify the template to render (index.html)

# Define a view for displaying items within a specific To-Do List
class ItemListView(ListView):
    model = ToDoItem  # Specify the model to use for this view (ToDoItem)
    template_name = "todo_app/todo_list.html"  # Specify the template to render (todo_list.html)

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

# Define a view for creating a new To-Do List
class ListCreate(CreateView):
    model = ToDoList  # Specify the model to use for this view (ToDoList)
    fields = ["title"]  # Define the fields to be used in the form

    # Override get_context_data to pass custom context (like the page title)
    def get_context_data(self):
        context = super(ListCreate, self).get_context_data()  # Get existing context data
        context["title"] = "Add a new list"  # Add a custom title to the context
        return context  # Return the updated context

# Define a view for creating a new To-Do Item within a specific To-Do List
class ItemCreate(CreateView):
    model = ToDoItem  # Specify the model to use for this view (ToDoItem)
    fields = [
        "todo_list",    # Field for selecting the To-Do List this item belongs to
        "title",        # Field for item title
        "description",  # Field for item description
        "due_date",     # Field for item due date
    ]

    # Override get_initial to pre-populate the form with the specific To-Do List
    def get_initial(self):
        initial_data = super(ItemCreate, self).get_initial()  # Get default initial data
        todo_list = ToDoList.objects.get(id=self.kwargs["list_id"])  # Get the current To-Do List
        initial_data["todo_list"] = todo_list  # Pre-fill the To-Do List field in the form
        return initial_data  # Return the updated initial data

    # Override get_context_data to include the specific To-Do List and custom title in the context
    def get_context_data(self):
        context = super(ItemCreate, self).get_context_data()  # Get existing context data
        todo_list = ToDoList.objects.get(id=self.kwargs["list_id"])  # Get the current To-Do List
        context["todo_list"] = todo_list  # Add the To-Do List to the context
        context["title"] = "Create a new item"  # Add a custom title to the context
        return context  # Return the updated context

    # Override get_success_url to redirect the user back to the To-Do List view after creation
    def get_success_url(self):
        return reverse("list", args=[self.object.todo_list_id])  # Redirect to the To-Do List view

# Define a view for updating an existing To-Do Item
class ItemUpdate(UpdateView):
    model = ToDoItem  # Specify the model to use for this view (ToDoItem)
    fields = [
        "todo_list",    # Field for selecting the To-Do List this item belongs to
        "title",        # Field for item title
        "description",  # Field for item description
        "due_date",     # Field for item due date
    ]

    # Override get_context_data to include the current To-Do List and custom title in the context
    def get_context_data(self):
        context = super(ItemUpdate, self).get_context_data()  # Get existing context data
        context["todo_list"] = self.object.todo_list  # Add the current To-Do List to the context
        context["title"] = "Edit item"  # Add a custom title to the context
        return context  # Return the updated context

    # Override get_success_url to redirect the user back to the To-Do List view after update
    def get_success_url(self):
        return reverse("list", args=[self.object.todo_list_id])  # Redirect to the To-Do List view

# Define a view for deleting an existing To-Do List
class ListDelete(DeleteView):
    model = ToDoList  # Specify the model to use for this view (ToDoList)
    success_url = reverse_lazy("index")  # Redirect to the index after list deletion

# Define a view for deleting an existing To-Do Item
class ItemDelete(DeleteView):
    model = ToDoItem  # Specify the model to use for this view (ToDoItem)

    # Override get_success_url to redirect the user back to the To-Do List after item deletion
    def get_success_url(self):
        # Redirect to the To-Do List view after the item is deleted
        return reverse_lazy("list", args=[self.kwargs["list_id"]])

    # Override get_context_data to add the current To-Do List to the context
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # Get the existing context data
        context["todo_list"] = self.object.todo_list  # Add the current To-Do List to the context
        return context  # Return the updated context
