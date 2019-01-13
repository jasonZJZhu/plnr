from django.shortcuts import render, redirect
from .models import Challenge

def home(request):
	return render(request, 'interface/home.html', {'title': ''})

def progress(request):
	context = {
		'challenges': Challenge.objects.all()
	}
	return render(request, 'interface/progress.html', context)
