from django.http import HttpResponse, Http404
from django.template import loader

from .models import Student

def index(request):
    return HttpResponse("<h1>Users page</h1>")

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
    return None