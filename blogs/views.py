from django import http
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, HttpResponse, redirect
# Create your views here.
def root (request):
    return redirect("blogs/") 
def index(request):
    return HttpResponse("placeholder para luego mostrar una lista de todos los blogs")
def new(request):
    return HttpResponse("placeholder para mostrar un nuevo formulario para crear un nuevo blog")
def create(request):
    return redirect("/blogs/")
def show(request,val):
    return HttpResponse(f'placeholder para mostrar el blog numero:{val}')
def edit(request,val):
    return HttpResponse(f'placeholder para editar el blog {val}')
def destroy(request,val):
    return redirect("/blogs/")
def json(request):
    dato =[{'name': 'Peter', 'email': 'peter@example.org'},
        {'name': 'Julia', 'email': 'julia@example.org'}]
    return JsonResponse(dato,safe=False)