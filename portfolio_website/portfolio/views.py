from django.shortcuts import render

# Create your views here.

def hhome (request):
    return render(request, '2.html')


def About(request):
    return render(request, 'about.html')

def Projects(request):
    return render(request, 'projects.html')

def Home(request):
    return render(request,'2.html')
