from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello everyone! Our Training has come to an end.Wishing everyone all the best for future.")
