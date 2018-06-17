from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):

    posts_count = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()

    def get_posts_count(self, obj):
        return obj.user_posts.count()

    def get_comments_count(self, obj):
        return Comment.objects.filter(post__user=obj).count()

    class Meta:
        model = User
        fields = ('pk', 'url', 'name', 'posts_count', 'comments_count', 'user_posts')

    def create(self, validated_data):
        posts_data = validated_data.pop('user_posts')
        post = Post.objects.create(**validated_data)
        for post_data in posts_data:
            Post.objects.create(post=post, **post_data)
        return post


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Comment
        fields = ('url', 'name', 'email', 'body', 'post')


class PostSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='name')
    comments_count = serializers.SerializerMethodField()

    def get_comments_count(self, obj):
        return obj.comments_in_post.count()

    class Meta:
        model = Post
        fields = ('user', 'url', 'title', 'body', 'comments_count')