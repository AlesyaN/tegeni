from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse("<h3>как говорили некоторые старейшины 'фак ю бич,соси кирпич',я адресую это питону,потому что я смог это вывести</h3>")
# Create your views here.
