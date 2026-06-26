from django import forms

class StudentSearchForm(forms.Form):
    student_id = forms.CharField(label="Student ID", max_length=20)