from django.shortcuts import render

# Create your views here.


# to retrive and display all of the employee records
def employee_list(request):
    return render(request, "employee_register/employee_list.html")


# deal with get and post requests for insert and update operations. 
def employee_form(request):
    return render(request, "employee_register/employee_form.html")


# for deleting an employee record
def employee_delete(request):
    return


# to configure the routing you go to the urls.py in the project