from rest_framework import viewsets, generics, permissions
from rest_framework.response import Response
from rest_framework_extensions.mixins import NestedViewSetMixin
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.throttling import ScopedRateThrottle
from django.http import JsonResponse
from django.db import transaction
from perfil.permissions import *
from config import settings
from .serializers import *
from .models import *
import json, os

# Create your views here.


class UserRootView(viewsets.ModelViewSet, NestedViewSetMixin):
    queryset = User.objects.all()
    serializer_class = UserCountSerializer
    http_method_names = ['get']
    name = 'user-root-list'


class UserView(viewsets.ModelViewSet, NestedViewSetMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'
    http_method_names = ['get']
    permission_classes = (UserReadOnly, permissions.IsAuthenticated)

    def get_queryset(self):
        try:
            return User.objects.filter(user=self.kwargs['user'])
        except:
            return User.objects.all()


class PostView(viewsets.ModelViewSet, NestedViewSetMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name = 'post-list'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerPostOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        try:
            return Post.objects.filter(owner=self.kwargs['user'])
        except:
            return Post.objects.all()


class CommentView(viewsets.ModelViewSet, NestedViewSetMixin):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    name = 'comment-list'
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerCommentOrReadOnly)

    def get_queryset(self):
        try:
            return Comment.objects.filter(post=self.kwargs['post'])
        except:
            return Comment.objects.all()


class ApiRoot(generics.GenericAPIView, NestedViewSetMixin):

    def get(self, request, *args, **kwargs):
        return Response({
            'users': reverse(UserView.name, request=request),
            'posts': reverse(PostView.name, request=request),
            'comments': reverse(CommentView.name, request=request),
            'reset-data': reverse('reset-data',request=request)
        })

class CustomAuthToken(ObtainAuthToken):

    throttle_scope = 'api-token'
    throttle_classes = (ScopedRateThrottle, )

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'user_id': user.id,
            'user_name': user.username,
            'token': token.key,
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
            User.save_from_json(**user)

        for post in file_content['posts']:

            Post.save_from_json(**post)

        for comment in file_content['comments']:
            Comment.save_from_json(**comment)

        return JsonResponse({'error': 'Ok sem Erros...'})
    except Exception as e:
        return JsonResponse({'error': str(e)})