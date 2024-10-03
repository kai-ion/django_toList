from django.utils import timezone
from django.db import models
from django.urls import reverse

# Helper function to return a date one week from the current time
def one_week_hence():
    return timezone.now() + timezone.timedelta(days=7)

# Model representing a To-Do List
class ToDoList(models.Model):
    # Title of the to-do list (must be unique, limited to 100 characters)
    title = models.CharField(max_length=100, unique=True)

    # Method to get the URL for viewing a specific to-do list based on its ID
    def get_absolute_url(self):
        return reverse("list", args=[self.id])

    # String representation of the model (shows the title of the list)
    def __str__(self):
        return self.title

# Model representing individual To-Do Items within a To-Do List
class ToDoItem(models.Model):
    # Title of the to-do item (limited to 100 characters)
    title = models.CharField(max_length=100)
    
    # Optional detailed description for the to-do item (can be left blank)
    description = models.TextField(null=True, blank=True)
    
    # Automatically sets the creation date and time when the to-do item is created
    created_date = models.DateTimeField(auto_now_add=True)
    
    # Due date for the to-do item (defaults to one week from the current time)
    due_date = models.DateTimeField(default=one_week_hence)
    
    # ForeignKey linking the to-do item to a specific to-do list (deletes the item if the list is deleted)
    todo_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)

    # Method to get the URL for updating a specific to-do item based on its list and item IDs
    def get_absolute_url(self):
        return reverse("item-update", args=[str(self.todo_list.id), str(self.id)])

    # String representation of the model (shows the title and due date of the item)
    def __str__(self):
        return f"{self.title}: due {self.due_date}"

    # Meta class to specify additional options for the model
    class Meta:
        # Orders the to-do items by their due date in ascending order
        ordering = ["due_date"]
