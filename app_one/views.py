from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse, redirect
# Create your views here.
def root (request):
    return redirect("/blogs") 
def index(request):
    return HttpResponse("placeholder para luego mostrar una lista de todos los blogs")