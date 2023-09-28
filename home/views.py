from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest

def MyHomePage(request: HttpRequest):
    return render(request, 'home/Homepage.html')