from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'url', 'username', 'user_posts')


class UserCountSerializer(serializers.ModelSerializer):
    posts_count = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()

    def get_posts_count(obj):
        return obj.user_posts.count()

    def get_comments_count(obj):
        return Comment.objects.filter(post__owner=obj).count()

    class Meta:
        model = User
        fields = ('id', 'username', 'posts_count', 'comments_count')


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ('url', 'name', 'email', 'body', 'post')


class PostSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')
    comments_count = serializers.SerializerMethodField()

    @staticmethod
    def get_comments_count(obj):
        return obj.comments_in_post.count()

    class Meta:
        model = Post
        fields = ('owner', 'url', 'title', 'body', 'comments_count')
