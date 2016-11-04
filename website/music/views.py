from django.shortcuts import render
# Python functions - user is going to request an url

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1> This is the music app homepage</h1>")