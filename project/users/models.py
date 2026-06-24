from django.db import models

from branches.models import Faculty

class Student(models.Model):

    def __str__(self):
        return self.student_id + ", " + self.first_name + " " + self.last_name
    
    def get_account_balance(self):
        return self.account_balance + " tenge"

    student_id = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, default=Faculty.get_default_faculty)
    account_balance = models.DecimalField(max_digits=20, decimal_places=6)

class Teacher(models.Model):    
    employee_id = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    # faculty = models.CharField()
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, default=Faculty.get_default_faculty)
    salary = models.DecimalField(max_digits=20, decimal_places=6)

    def __str__(self):
        return self.employee_id + ", " + self.first_name + " " + self.last_name
    
