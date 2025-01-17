from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee

# Create your views here.


# to retrive and display all of the employee records
def employee_list(request):
    context = {
        "employee_list": Employee.objects.all()
    }  # get all employee records from the database as a list
    return render(request, "employee_register/employee_list.html", context)


# deal with get and post requests for insert and update operations.
def employee_form(request, id=0):

    if request.method == "GET":

        if id == 0:  # if id is 0, it means we are inserting a new employee record
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(
                pk=id
            )  # get the employee record with the id
            form = EmployeeForm(instance=employee)
        return render(request, "employee_register/employee_form.html", {"form": form})
    else:
        if id == 0:

            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(
                pk=id
            )  # get the employee record with the id
            form = EmployeeForm(request.POST, instance=employee)

        if form.is_valid():
            form.save()
        return redirect("/employee/list")


# for deleting an employee record
def employee_delete(request, id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect("/employee/list")


# to configure the routing you go to the urls.py in the project
