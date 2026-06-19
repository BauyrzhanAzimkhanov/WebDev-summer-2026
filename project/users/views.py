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
        raise Http404("Student doesn\'t exists.\nFix your URL!")
    template = loader.get_template("users/index.html")
    context = {"user": user}
    return HttpResponse(template.render(context, request))

def users(requests):
    return None