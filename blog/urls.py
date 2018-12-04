from django.urls import path
from . import views
urlpatterns = [
    # 127.0.0.1:8000 --> local
    # mydjangosite.com --> online
    path('', views.postsList, name='postsList'),
    # 127.0.0.1:8000/post/2 --> local
    # mydjangosite.com/post/2 --> online
    path('post/<int:pk>/', views.postsDetail, name='postsDetail'),
    # 127.0.0.1:8000/post/new --> local
    # mydjangosite.com/post/new--> online
    path('post/new/', views.postNew, name='postNew'),
    # 127.0.0.1:8000/post/1/edit --> local
    # mydjangosite.com/post/1/edit--> online
    path('post/<int:pk>/edit/', views.postEdit, name='postEdit'),
    # 127.0.0.1:8000/drafts --> local
    # mydjangosite.com/drafts--> online
    path('drafts/', views.postDraftlist, name='postDraftlist'),
    # 127.0.0.1:8000/post/1/publish --> local
    # mydjangosite.com/post/1/publish--> online
    path('post/<int:pk>/publish/', views.postPublish, name='postPublish')
]
