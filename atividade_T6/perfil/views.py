from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication, BaseAuthentication
from rest_framework.authtoken.views import ObtainAuthToken, Token
from rest_framework_extensions.mixins import NestedViewSetMixin
from rest_framework import viewsets, generics, permissions
from rest_framework.response import Response
from rest_framework.throttling import ScopedRateThrottle
from rest_framework import exceptions
from perfil.permissions import *
from .serializers import *
from .models import *


class UserView(viewsets.ModelViewSet, NestedViewSetMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'
    http_method_names = ['get']

    authentication_classes = (
        TokenAuthentication, 
        SessionAuthentication, 
        BasicAuthentication
        )

    permission_classes = (UserReadOnly, permissions.IsAuthenticated)


class CharacterView(viewsets.ModelViewSet, NestedViewSetMixin):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    name = 'character-list'

    authentication_classes = (
        TokenAuthentication, 
        SessionAuthentication, 
        BasicAuthentication
        )

    permission_classes = (permissions.IsAuthenticatedOrReadOnly)


class ItenView(viewsets.ModelViewSet, NestedViewSetMixin):
    queryset = item.objects.all()
    serializer_class = ItemSerializer
    name = 'item-list'

    authentication_classes = (
        TokenAuthentication, 
        SessionAuthentication, 
        BasicAuthentication
        )

    permission_classes = (permissions.IsAuthenticatedOrReadOnly)

    #def get_queryset(self):
    #    try:
    #        return Comment.objects.filter(post=self.kwargs['post'])
    #    except:
    #        return Comment.objects.all()


class MusicView(viewsets.ModelViewSet, NestedViewSetMixin):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    name = 'music-list'

    authentication_classes = (
        TokenAuthentication, 
        SessionAuthentication, 
        BasicAuthentication
        )

    permission_classes = (permissions.IsAuthenticatedOrReadOnly)

    #def get_queryset(self):
    #    try:
    #        return Comment.objects.filter(post=self.kwargs['post'])
    #    except:
    #        return Comment.objects.all()

class AreaView(viewsets.ModelViewSet, NestedViewSetMixin):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer
    name = 'area-list'

    authentication_classes = (
        TokenAuthentication, 
        SessionAuthentication, 
        BasicAuthentication
        )

    permission_classes = (permissions.IsAuthenticatedOrReadOnly)

    #def get_queryset(self):
    #    try:
    #        return Comment.objects.filter(post=self.kwargs['post'])
    #    except:
    #        return Comment.objects.all()


class ApiRoot(generics.GenericAPIView, NestedViewSetMixin):

    def get(self, request, *args, **kwargs):
        return Response({
            'users': reverse(UserView.name, request=request),
            'characters': reverse(CharacterView, request=request),
            'itens': reverse(ItenView, request=request),
            'musics': reverse(MusicView, request=request),
        })

class TokenAcess(ObtainAuthToken):
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


class TokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        username = request.META.get('user_name')
        if not username:
            return None
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')

        return (user, None)