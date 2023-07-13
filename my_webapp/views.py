from django.shortcuts import render, HttpResponse


def home (request):
    return HttpResponse("This is my django website")

def about (request):
    return HttpResponse("about me")

def contact (request):
    return HttpResponse("contact me")