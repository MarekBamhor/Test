from django.shortcuts import render


def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def plans(request):
    return render(request, "plans.html")

def famtree(request):
    return render(request, "famtree.html")

def contact(request):
    return render(request, "contact.html")
