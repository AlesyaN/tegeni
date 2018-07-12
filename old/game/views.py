from django.shortcuts import render

def gameRules(request):
    return render( request , "game/gameRules.html" )
