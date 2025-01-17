from django.urls import path
from . import views

# """Relative Import: The dot is a relative import, meaning it tells Python to look for the views.py file in the current directory (the same directory as the file from which you're importing)."""

urlpatterns = [
    path(
        "", views.employee_form, name="employee_insert"
    ),  # for get and post request for insert operation
    path(
        "<int:id>/", views.employee_form, name="employee_update"
    ),  # for get and port request for update operation
    path(
        "list/", views.employee_list, name="employee_list"
    ),  # get request to retrieve and display all records.
    # localhost:p/employee/list
    path("delete/<int:id>/", views.employee_delete, name="employee_delete"),
]
