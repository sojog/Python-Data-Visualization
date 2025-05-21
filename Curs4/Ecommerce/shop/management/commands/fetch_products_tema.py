

## Luati 1 produs si il puneti in DB
##         (nume, pret, imagine...)

## Luati 10 produse si le pune in DB


from django.core.management.base import BaseCommand, CommandError 
from django.core.files.base import ContentFile
from shop.models import Product, Category
import requests

### python manage.py fetch_product_tema
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


            image_url = prod_dict["thumbnail"]
            image_response = requests.get(image_url)

            image_content = image_response.content

            product = Product(name=name, slug=slug, description=description, price=price)


            category_name = prod_dict["category"]
            print("Category_name:", category_name)
            category_object = Category.objects.filter(name=category_name.title()).first()

            if category_object:
                product.category = category_object
                print("A gasit categoria..")


            product.image.save(name, ContentFile(image_content))

            product.save()

        print("S-a terminat...")