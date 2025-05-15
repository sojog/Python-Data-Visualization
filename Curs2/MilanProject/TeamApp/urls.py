from django.urls import path
from .views import all_players_view

urlpatterns = [

	path("all", all_players_view),
]
