from django.http import HttpResponse
def index(request):
    return HttpResponse("Hi this is Kyle's Index")