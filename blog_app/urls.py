from django.urls import path, include
from blog_app.views import Home, GetPost, PostsByCategory, PostsByTag, Search

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('category/<str:slug>/', PostsByCategory.as_view(), name='category'),
    path('post/<str:slug>/', PostsByTag.as_view(), name='tag'),
    path('tag/<str:slug>/', GetPost.as_view(), name='post'),
    path('search/', Search.as_view(), name='search'),
]
