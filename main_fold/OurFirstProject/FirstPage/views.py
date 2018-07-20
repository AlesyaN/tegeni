from django.shortcuts import render

def HelloPage(request):
    return render(request , "firstPage/HelloPage.html" )
