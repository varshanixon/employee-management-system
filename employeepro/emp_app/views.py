from django.shortcuts import render,redirect

from django.views.generic import View

from emp_app.forms import EmployeeForm

from emp_app.models import Employee

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
    

class EmployeeListView(View):

    template_name = "emp_list.html"

    def get(self,request,*args,**kwargs):

        qs = Employee.objects.all()

        return render(request,self.template_name,{"data":qs})
    

class EmployeeDetailView(View):

    template_name = "emp_detail.html"

    def get(self,request,*args,**kwargs):

        # extract pk from url
        id = kwargs.get("pk")

        qs = Employee.objects.get(id=id)

        return render(request,self.template_name,{"data":qs})
    


