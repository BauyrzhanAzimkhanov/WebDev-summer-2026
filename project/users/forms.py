from django import forms
from django.forms import ModelForm
from .models import Student

class StudentSearchForm(forms.Form):
    student_id = forms.CharField(label="Student ID", max_length=20)

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ["student_id", "first_name", "second_name", "last_name", "faculty", "account_balance"]