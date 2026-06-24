from django.db import models
# from users.models import Teacher

class Faculty(models.Model):
    class Meta:
        verbose_name_plural = "Faculties"

    name = models.CharField()
    dean = models.ForeignKey("users.Teacher", on_delete=models.CASCADE, related_name="+")

    def get_default_faculty():
        return Faculty.objects.get(name__exact = "SITE").id
    
    def __str__(self):
        return self.name