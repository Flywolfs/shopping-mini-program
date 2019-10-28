from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def wxconn(request):
    print(request)
    return HttpResponse("Good Request!")
