from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'username', 'user_posts')


class CharacterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'name', 'raca', 'characterType', 'native', 'musicTheme')


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Comment
        fields = ('url', 'name', 'itemClass', 'effect', 'patter', 'location', 'cost')


class MusicSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Address
        fields = ('url', 'name')