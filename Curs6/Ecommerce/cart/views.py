from django.shortcuts import render, redirect
import pandas as pd
# Create your views here.

def cart_view(request):
	try:
		df = pd.read_csv("produse_salvate.csv")
	except:
		df = pd.DataFrame({"produse":[]})

	context = {"produse":df}
	return render(request, 'cart.html', context)

def add_to_cart_view(request, slug):
	print("Ar trebui adaugat in cos..", slug)

	print("Sesiunea curenta:", request.session)


	return redirect("cart_url")