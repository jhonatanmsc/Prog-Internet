"""
Book: Building RESTful Python Web Services
Chapter 2: Working with class based views and hyperlinked APIs in Django
Author: Gaston C. Hillar - Twitter.com/gastonhillar
Publisher: Packt Publishing Ltd. - http://www.packtpub.com
"""
from rest_framework import generics, response
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import Game, GameCategory, Player, Score
from .serializers import GameSerializer
from .serializers import PlayerSerializer
from .serializers import ScoreSerializer
from .serializers import GameCategorySerializer


class GameCategoryList(generics.ListCreateAPIView):
	queryset = GameCategory.objects.all()
	serializer_class = GameCategorySerializer
	name = 'gamecategory-list'


class GameCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = GameCategory.objects.all()
	serializer_class = GameCategorySerializer
	name = 'gamecategory-detail'


class GameList(generics.ListCreateAPIView):
	queryset = Game.objects.all()
	serializer_class = GameSerializer
	name = 'game-list'


class GameDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Game.objects.all()
	serializer_class = GameSerializer
	name = 'game-detail'


class PlayerList(generics.ListCreateAPIView):
	queryset = Player.objects.all()
	serializer_class = PlayerSerializer
	name = 'player-list'


class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Player.objects.all()
	serializer_class = PlayerSerializer
	name = 'player-detail'


class ScoreList(generics.ListCreateAPIView):
	queryset = Score.objects.all()
	serializer_class = ScoreSerializer
	name = 'score-list'


class ScoreDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Score.objects.all()
	serializer_class = ScoreSerializer
	name = 'score-detail'


class ApiRoot(generics.GenericAPIView):
	name = 'api-root'

	def get(self, request, *args, **kwargs):

		return Response({
			'players': reverse(PlayerList.name, request=request),
			'game-categories': reverse(GameCategoryList.name, request=request),
			'games': reverse(GameList.name, request=request),
			'scores': reverse(ScoreList.name, request=request)
		})