from django.db import models

# Create your models here.

class Employee(models.Model):

    name = models.CharField(max_length=50)

    email = models.EmailField(unique=True)

    address = models.TextField()

    department = models.CharField(max_length=100)

    salary = models.PositiveIntegerField()

    date_of_join = models.DateField()

    GENDER_OPTIONS = (
        ('male','male'),
        ('female',('female')),
    )

    gender = models.CharField(max_length=50,choices=GENDER_OPTIONS,default="male")

    dob = models.DateField()

    picture = models.ImageField(upload_to="emp_images",null=True,blank=True)

    def __str__(self):
        
        return self.name
    

