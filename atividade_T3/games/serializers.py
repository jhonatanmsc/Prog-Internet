from rest_framework import serializers
from .models import Game, Score, Player, GameCategory
from datetime import date


class GameCategorySerializer(serializers.HyperlinkedModelSerializer):
	
	class Meta:
		model = GameCategory
		fields = ('url', 'pk', 'name', 'games')


class GameSerializer(serializers.HyperlinkedModelSerializer):
	#game_category = serializers.SlugRelatedField(queryset=GameCategory.objects.all(), slug_field='name')
	class Meta:
		model = Game
		fields = (
			'url',
			'pk',
			'name', 
			'release_date', 
			'game_category',
		)


class ScoreSerializer(serializers.HyperlinkedModelSerializer):
	game = serializers.SlugRelatedField(queryset=Game.objects.all(), slug_field='name')
	player = serializers.SlugRelatedField(queryset=Player.objects.all(), slug_field='name')

	class Meta:
		model = Score
		fields = (
			'url',
			'pk',
			'score',
			'score_date',
			'player',
			'game',
		)

	def validate(self, data):

		#if data['player'] == None or data['game'] == None:
		#	raise serializers.ValidationError("Player e Game não podem estar vazios!!")

		if data['score'] < 0:
			raise serializers.ValidationError("Score não pode ser negativo!!")

		if data['score_date'] > date.today():
			raise serializers.ValidationError("A data do Score não pode estar no futuro!!")
		
		return data

class PlayerSerializer(serializers.HyperlinkedModelSerializer):
	scores = ScoreSerializer(many=True, read_only=True)

	class Meta:
		model = Player
		fields = (
			'url',
			'name',
			'gender',
			'scores',
		)