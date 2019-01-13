from django.shortcuts import render, redirect
from .models import Challenge

def home(request):
	return render(request, 'interface/home.html', {'title': 'Home'})

def progress(request):
	context = {
		'title': 'Progress',
		'challenges': Challenge.objects.all()
	}
	return render(request, 'interface/progress.html', context)
