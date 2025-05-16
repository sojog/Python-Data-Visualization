from django.urls import path
from .views import product_details_view
from .views import all_products_view

urlpatterns = [

	path("all", all_products_view),
	path("details", product_details_view),
]
