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
from django.urls import path, include
from rest_framework_nested import routers
from perfil.views import *
from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token

app_name='perfil'
urlpatterns = [
    path('', ApiRoot.as_view(), name='api-root'),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('reset-data', reset_data, name='reset-data'),
    path('api-obtain-token/', TokenAcess.as_view(), name='api-token'),
]

router = routers.DefaultRouter()
router.register(r'users-root', UserRootView)
router.register(r'users', UserView)
router.register(r'posts', PostView)
router.register(r'comments', CommentView)

user_router = routers.NestedSimpleRouter(router, r'users', lookup='user')
user_router.register(r'posts', PostView, base_name='users_posts')

posts_router = routers.NestedSimpleRouter(user_router, r'posts', lookup='post')
posts_router.register(r'comments', CommentView, base_name='comments_posts')

urlpatterns += router.urls
urlpatterns += user_router.urls
urlpatterns += posts_router.urls