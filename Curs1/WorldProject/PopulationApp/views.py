from django.shortcuts import render

# Create your views here.

def all_countries_view(request):
	context = {}
	return render(request, 'all_countries.html', context)

def choose_countries_view(request):
	context = {}
	return render(request, 'choose_countries.html', context)
