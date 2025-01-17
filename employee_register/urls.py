from django.urls import path
from . import views

# """Relative Import: The dot is a relative import, meaning it tells Python to look for the views.py file in the current directory (the same directory as the file from which you're importing)."""

urlpatterns = [
    path("", views.employee_form),
    path("list/", views.employee_list),  # localhost:p/employee/list
]
