from django.db import models


class Student(models.Model):

    # def __str__(self):
    #     return self.student_id + ", " + self.first_name + " " + self.last_name
    
    def get_account_balance(self):
        return self.account_balance + " tenge"

    student_id = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    faculty = models.CharField()
    account_balance = models.DecimalField(max_digits=20, decimal_places=6)