from django.shortcuts import render

from django.views.generic import View

from emp_app.forms import EmployeeForm

# Create your views here.

class EmployeeCreateView(View):

    template_name = "emp_add.html"

    form_class = EmployeeForm

    def get(self,request,*args,**kwargs):

        # Create form instance
        form_instance = self.form_class

        # Render form into template
        return render(request,self.template_name,{'form':form_instance})