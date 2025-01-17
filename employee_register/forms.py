from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ("emp_code", "fullname", "mobile", "position")
        # i can easily change the order of these

        labels = {
            "fullname": "Full Name",
            "mobile": "Mobile",
            "position": "Postition",
            "emp_code": "EMP code",
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields["position"].empty_label = "Select"
        self.fields["emp_code"].required = False
