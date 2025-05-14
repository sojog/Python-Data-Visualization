from django.shortcuts import render
import matplotlib.pyplot as plt
# Create your views here.
from io import BytesIO
import base64
import matplotlib

matplotlib.use("svg")

def all_countries_view(request):
	context = {}
	return render(request, 'all_countries.html', context)


def create_image(countries = ["China", "India", "Brazil"], population = [1411, 1378, 213]):

	fig, axes = plt.subplots()
	axes.pie(population, labels=countries);

	buffer = BytesIO()
	fig.savefig(buffer, format="png")
	buffer.seek(0)
	image_png = buffer.getvalue()
	buffer.close()

	return base64.b64encode(image_png).decode("utf-8")


def choose_countries_view(request):
	countries = ['Bangladesh', 'Brazil', 'China', 'India', 'Indonesia', 'Mexico', 'Nigeria', 'Pakistan', 'Russia', 'United States']
	population =  [170, 213, 1411, 1378, 271, 126, 211, 225, 146, 331]


	result_image = '10_tari.png'
	base64_image = None
	tari = None

	if request.method == "POST":
		print("parametri:", request.POST.keys())
		tari = request.POST.keys()
		print("tarile primite:", tari)

		tari = [t for t in tari if t in countries]
		locuitori = [ population[countries.index(t)] for t in tari ]

		base64_image = create_image(tari, locuitori)
	

	context = {
		"countries": countries,
		"result_image": result_image,
		"base64_image":base64_image,
		'tari': tari 
	}
	return render(request, 'choose_countries.html', context)
