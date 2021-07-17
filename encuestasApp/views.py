from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Encuestas Index")
def new(request):
    return HttpResponse("New encuestas")