from django.shortcuts import render

# Create your views here.

def HelloPage(request):
    return render(request , "mainPage/index.html" )
