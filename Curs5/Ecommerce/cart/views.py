from django.shortcuts import render
import pandas as pd
# Create your views here.

def cart_view(request):
	try:
		df = pd.read_csv("produse_salvate.csv")
	except:
		df = pd.DataFrame({"produse":[]})

	context = {"produse":df}
	return render(request, 'cart.html', context)
