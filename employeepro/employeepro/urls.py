"""
URL configuration for employeepro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from emp_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('employee/add/',views.EmployeeCreateView.as_view(),name="employee-add"),

    path('employee/all/',views.EmployeeListView.as_view(),name="employee-list"),

    path('employee/<int:pk>/',views.EmployeeDetailView.as_view(),name="employee-detail"),

    path('employee/<int:pk>/remove/',views.EmployeeRemoveView.as_view(),name="employee-remove"),

    path('employee/<int:pk>/modify/',views.EmployeeUpdateView.as_view(),name="employee-update"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
