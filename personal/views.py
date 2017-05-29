from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
	return render(request, 'personal/home.html')


def profile(request):
	return render(request, 'personal/profile.html')


def about(request):
	return render(request, 'personal/about.html')

def contact(request):
	return render(request, 'personal/contact.html')


