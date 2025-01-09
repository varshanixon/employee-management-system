from django.shortcuts import render,redirect

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
    
    def post(self,request,*args,**kwargs):

        # Extract form_data
        form_data = request.POST

        # Initialize form with form_data
        form_instance = self.form_class(form_data,files=request.FILES)

        # Check if form has errors
        if form_instance.is_valid():

            # Save form_instance
            form_instance.save()

            return redirect("employee-add")
        
        return render(request,self.template_name,{"form":form_instance})
    