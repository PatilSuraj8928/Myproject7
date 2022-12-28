from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return HttpResponse('<h1>This is string from app1 first Function</h1>')

def string2(request):
    return HttpResponse('<center><h1>This is string 2 of app1</h1></center>')