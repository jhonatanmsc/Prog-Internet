from rest_framework import viewsets, generics, permissions
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from django.http import JsonResponse
from django.db import transaction
from perfil.permissions import *
from config import settings
from .serializers import *
import json, os

# Create your views here.
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name = 'post-list'

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name = 'post-detail'


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    name = 'comment-list'


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    name = 'comment-detail'

class UserPostDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        try:
            user = User.objects.get(pk=self.kwargs.get('pk', None))
        except User.DoesNotExist:
            user = None

        posts = Post.objects.filter(user=user.id)
        indice = int(self.kwargs['post_id'])
        post = posts[indice - 1]
        return Post.objects.get(pk = post.id)


class UserPostCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        try:
            user = User.objects.get(pk=self.kwargs.get('pk', None))
        except User.DoesNotExist:
            user = None

        posts = Post.objects.filter(user=user.id)
        post = posts.get(pk=self.kwargs.get('post_id', None))
        comment = post.comments_in_post.filter(pk=self.kwargs.get('comment_id', None))
        return comment


class UserPostComments(generics.ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        try:
            user = User.objects.get(pk=self.kwargs.get('pk', None))
        except User.DoesNotExist:
            user = None

        posts = Post.objects.filter(user=user.id)
        post = posts.get(pk=self.kwargs.get('post_id', None))
        comments = post.comments_in_post.all()
        return comments


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'users': reverse(UserList.name, request=request),
            'posts': reverse(PostList.name, request=request),
            'comments': reverse(CommentList.name, request=request),
            'reset-data': reverse('reset-data',request=request)
        })


@transaction.atomic
def reset_data(request):
    try:
        # Clearing previous data:
        Address.objects.all().delete() 
        User.objects.all().delete() 

        # Loading the file:
        file = open(os.path.join(settings.PROJECT_DIR, 'personal_database.json'))
        read_file = json.dumps(file.read())
        file.close()
        file_content =  eval(json.loads(read_file))
        print(len(file_content['users']))
        # Saving one by one:
        for user in file_content['users']:
            print(user)
            User.save_from_json(**user)
        print('LOL 1')
        for post in file_content['posts']:

            Post.save_from_json(**post)
        print('LOL 2')
        for comment in file_content['comments']:
            Comment.save_from_json(**comment)
        print('LOL 3')
        return JsonResponse({'error': False})
    except Exception as e:
        return JsonResponse({'error': str(e)})