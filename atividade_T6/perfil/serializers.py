from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'username')


class CharacterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Character
        fields = ('url', 'name', 'race', 'characterType', 'native', 'musicTheme')


class ItemSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Item
        fields = ('url', 'name', 'itemClass', 'effect', 'pattern', 'location', 'cost')


class MusicSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Music
        fields = ('url', 'name')


class AreaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Area
        fields = ('url', 'name')