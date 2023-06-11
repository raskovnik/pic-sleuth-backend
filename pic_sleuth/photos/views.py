from django.http import HttpResponse


# Create your views here.
def HelloView(request):
    return HttpResponse("Hello, World!")
