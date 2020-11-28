from django.http import HttpResponse

# Create your views here.
#index means main page of this app
def index(request):
    return HttpResponse('Hello World')