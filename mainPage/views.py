from django.shortcuts import render

# Create your views here.

def startPage(request):
    return render(request , "mainPage/starterPage.html" )
