from django.shortcuts import render

def index(request):
    return render(request, "jobs/index.html")


def role(request):
    return render(request, "role/index.html")