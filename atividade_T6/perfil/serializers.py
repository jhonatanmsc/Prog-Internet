from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('url', 'username', 'user_posts')