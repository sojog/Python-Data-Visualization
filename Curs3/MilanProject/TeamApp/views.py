from django.shortcuts import render

# Create your views here.

from .models import Player


def all_players_view(request):
	players = Player.objects.all()

	context = {
		"players":players
	}
	return render(request, 'all_players.html', context)
