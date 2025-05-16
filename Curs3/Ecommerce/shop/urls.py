from django.urls import path
from .views import category_details_view
from .views import all_categories_view
from .views import product_details_view
from .views import all_products_view

urlpatterns = [

	path("all", all_products_view),
	path("details", product_details_view),
	path("categories", all_categories_view),
	path("category", category_details_view),
]
