from django import forms

from emp_app.models import Employee

class EmployeeForm(forms.ModelForm):

    class Meta:

        model = Employee

        fields = "__all__"

        widgets ={
            "date_of_join" : forms.DateInput(attrs={"type":"date"}),
            "dob" : forms.DateInput(attrs={"type":"date"})
        }