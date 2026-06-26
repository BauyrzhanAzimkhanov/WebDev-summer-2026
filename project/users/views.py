from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader

from .models import Student
from .forms import StudentSearchForm

def index(request):
    students = Student.objects.all()
    template = loader.get_template("students/index.html")
    context = {"students": students}
    return HttpResponse(template.render(context, request))

def user_detalization(request, user_id):
    return HttpResponse("""<h1>User page</h1>
                        Current user is with id %s""" % user_id)
                        
def user_info(request, user_id):
    try:
        user = Student.objects.get(id__exact = user_id)
    except Student.DoesNotExist:
        template404 = loader.get_template("students/student_info_404.html")
        context = {"user_id": user_id}
        return HttpResponse(template404.render(context, request), status=404)
        # raise Http404("Student doesn\'t exists.\nFix your URL!")
    template = loader.get_template("students/student_info.html")
    context = {"user": user}
    return HttpResponse(template.render(context, request))

def users(requests):
    template = loader.get_template("students/index.html")
    return HttpResponse(template.render({}, requests))


def search_student(request):
    if request.method == "POST":
        form = StudentSearchForm(request.POST)
        if form.is_valid():
            stud_id = form.cleaned_data["student_id"]
            try:
                student = Student.objects.get(student_id=stud_id)
                return HttpResponseRedirect("../" + str(student.id))
            except Student.DoesNotExist:
                return HttpResponse("No student found")
    else:
        form = StudentSearchForm()
    template = loader.get_template("students/search.html")
    context = {"form": form}
    return HttpResponse(template.render(context, request))