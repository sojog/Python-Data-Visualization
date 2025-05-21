

## Luati 1 produs si il puneti in DB
##         (nume, pret, imagine...)

## Luati 10 produse si le pune in DB


from django.core.management.base import BaseCommand, CommandError
from shop.models import Product
import requests

### python manage.py fetch_product
class Command(BaseCommand):
    help = "Fetch product from https://dummyjson.com/products/product"

    def handle(self, *args, **options):
        BASE_URL = "https://dummyjson.com/"
        URL_PRODUCTS = BASE_URL + "products"

        LIMIT = 1

        response = requests.get(URL_PRODUCTS, {"limit":LIMIT})
        product_list = response.json()["products"]

        for prod_dict in product_list:

            name = prod_dict["title"]
            slug = name.lower().replace(" ", "-")
            description = prod_dict["description"] 
            
            price = prod_dict["price"]


            Product.objects.create(name=name, slug=slug, description=description, price=price)

        print("S-a terminat...")