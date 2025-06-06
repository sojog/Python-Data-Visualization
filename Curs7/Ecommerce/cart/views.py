from django.shortcuts import render, redirect
from  shop.models import Product 
# Create your views here.

class CartLogic:
	def __init__(self, request):
		self.request = request

		##  { "SLUG" : quantity }
		self.produse_existente = request.session.get("cos", { })

	### Totalul cartului

	@property
	def total_price(self):
		return sum( [product.price * quantity  for product, quantity in self.products.items()] )


	@property
	def number_of_products(self):
		return sum(self.produse_existente.values())


	### Produsele din cart si numarul lor


	@property
	def products_mai_putin_eficienta(self):
		product_slugs = self.produse_existente.keys()

		real_products = {  }
		for slug in product_slugs:
			produsul_efectiv = Product.objects.filter(slug=slug).first()
			real_products[produsul_efectiv] = self.produse_existente[slug]

		return real_products
	


	@property
	def products(self):
		product_slugs = self.produse_existente.keys()

		products_with_slugs = Product.objects.filter(slug__in=product_slugs)
		real_products = {  }

		for product in products_with_slugs:
			real_products[product] = self.produse_existente[product.slug]

		return real_products

	### Adaugare produs in cart
	def add(self, slug, quantity):

		existing_quantity = self.produse_existente.get(slug, 0)
		quantity += existing_quantity

		self.produse_existente[slug] =  quantity
		self.request.session["cos"] = self.produse_existente

	### Stergere produs din cart
	def remove(self, product):
		pass
	
	### Stergere cart
	def clear(self):
		pass









def cart_view(request):

	# TODO: 
	cart_logic = CartLogic(request)
	context = { 
			"cart":cart_logic
			
			}


	return render(request, 'cart.html', context)




def add_to_cart_view(request, slug):


	print("Ar trebui adaugat in cos..", slug)
	print("Sesiunea curenta:", request.session)
	
	print("Sesiune", request.POST)



	cart_logic = CartLogic(request)
	quantity = request.POST.get("quantity", 1)
	quantity = int(quantity)

	cart_logic.add(slug, quantity)
	


	return redirect("cart_url")