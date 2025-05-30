from django.shortcuts import render, redirect

# Create your views here.

class Cart:
	def __init__(self, request):
		self.request = request


def cart_view(request):

	## TODO:  cart = Cart(request)
	## cart.exising_products

	produse_existente = request.session.get("cos", { })
	context = {"produse":produse_existente}
	return render(request, 'cart.html', context)

def add_to_cart_view(request, slug):


	## TODO:  cart = Cart(request)



	print("Ar trebui adaugat in cos..", slug)
	print("Sesiunea curenta:", request.session)
	
	print("Sesiune", request.POST)


	produse_existente = request.session.get("cos", { })
	
	quantity = request.POST.get("quantity", 1)
	quantity = int(quantity)
	existing_quantity = produse_existente.get(slug, 0)
	quantity += existing_quantity
	produse_existente[slug] =  quantity
	request.session["cos"] = produse_existente



	return redirect("cart_url")