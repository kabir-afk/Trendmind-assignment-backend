from django.http import HttpResponse
from rest_framework.response import Response

def home(request):
    return HttpResponse("Home page")