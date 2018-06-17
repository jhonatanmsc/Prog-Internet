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

from perfil import views

app_name='perfil'
urlpatterns = [
    path('', views.ApiRoot.as_view(), name='api-root'),
    path('api-auth/', include('rest_framework.urls')),
    path('reset-data', views.reset_data, name='reset-data'),

    path('users/', views.UserList.as_view(), name=views.UserList.name),
    path('users/<int:pk>', views.UserDetail.as_view(), name=views.UserDetail.name),
    path('users/<int:pk>/posts/', views.UserDetail.as_view(), name='user-posts'),
    path('users/<int:pk>/posts/<int:post_id>', views.UserPostDetail.as_view(), name='user-post-detail'),
    path('users/<int:pk>/posts/<int:post_id>/comments/', views.UserPostComments.as_view(), name='user-post-comment'),
    path('users/<int:pk>/posts/<int:post_id>/comments/<int:comment_id>', views.UserPostCommentDetail.as_view(), name='user-post-comment-detail'),

    path('posts/', views.PostList.as_view(), name=views.PostList.name),
    path('posts/<int:pk>', views.PostDetail.as_view(), name=views.PostDetail.name),
    
    path('comments/', views.CommentList.as_view(), name=views.CommentList.name),
    path('comments/<int:pk>', views.CommentDetail.as_view(), name=views.CommentDetail.name),

]