"""atividade_T4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import path, include
from rest_framework_nested import routers
from perfil.views import *
from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView,)


app_name='perfil'
urlpatterns = [
    path('', ApiRoot.as_view(), name='api-root'),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    #path('api-obtain-token/', obtain_auth_token),
    #path('api-obtain-token2/', TokenAcess.as_view(), name='api-token'),
    url(r'^api/token/$', TokenObtainPairView.as_view(), name='token_obtain_pair'), #Paths do JWT
    url(r'^api/token/refresh/$', TokenRefreshView.as_view(), name='token_refresh'), #Paths do JWT
]

router = routers.DefaultRouter()
router.register(r'users', UserView)
router.register(r'characters', CharacterView)
router.register(r'itens', ItemView)
router.register(r'musics', MusicView)
router.register(r'areas', AreaView)

user_router = routers.NestedSimpleRouter(router, r'areas', lookup='name')
user_router.register(r'characters', CharacterView, base_name='areas_characters')
user_router.register(r'itens', ItemView, base_name='areas_itens')

urlpatterns += router.urls
urlpatterns += user_router.urls