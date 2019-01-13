from django.shortcuts import render, redirect

def home(request):
	return render(request, 'interface/home.html', {'title': 'Home'})

def progress(request):
	return render(request, 'interface/progress.html', {'title': 'Progress'})

def rewards(request):
	return render(request, 'interface/rewards.html', {'title': 'Rewards'})