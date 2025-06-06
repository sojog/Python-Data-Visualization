from django.urls import path
from .views import cart_view

from .views import add_to_cart_view

urlpatterns = [

	path("", cart_view, name="cart_url"),
    path("add/<slug>", add_to_cart_view, name="add_to_cart_url"),
]
