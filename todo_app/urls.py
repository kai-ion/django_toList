# todo_list/todo_app/urls.py

# Import necessary modules for defining URL patterns
from django.urls import path  # Import the path function for URL routing
from . import views  # Import views from the current app (todo_app)
from todo_app import views  # Import views again (optional, could be cleaned up)

# Define URL patterns for the application
urlpatterns = [
    # Home page route that displays all to-do lists using the ListListView
    path("", views.ListListView.as_view(), name="index"),
    
    # Route for viewing items in a specific to-do list, identified by the list_id
    path("list/<int:list_id>/", views.ItemListView.as_view(), name="list"),

    # CRUD patterns for ToDoLists (Create, Read, Update, Delete)
    # Route for adding a new to-do list using the ListCreate view
    path("list/add/", views.ListCreate.as_view(), name="list-add"),

    # CRUD patterns for ToDoItems (Create, Read, Update, Delete)
    # Route for adding a new item to a specific to-do list, identified by list_id
    path(
        "list/<int:list_id>/item/add/",  # URL with dynamic list_id to specify which list to add the item to
        views.ItemCreate.as_view(),  # Use the ItemCreate view for handling this request
        name="item-add",  # Name this route "item-add"
    ),

    # Route for updating an existing item in a to-do list, identified by list_id and item pk (primary key)
    path(
        "list/<int:list_id>/item/<int:pk>/",  # URL with dynamic list_id and pk to specify which item to update
        views.ItemUpdate.as_view(),  # Use the ItemUpdate view for handling this request
        name="item-update",  # Name this route "item-update"
    ),
]
