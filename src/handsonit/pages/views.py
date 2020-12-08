from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
	user = request.user;
	return render(request, "home.html", {'user':user})

def flinfo_view(request, *args, **kwargs):
	return render(request, "flinfo.html", {})

def binfo_view(request, *args, **kwargs):
	return render(request, "binfo.html", {})