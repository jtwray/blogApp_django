from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib import admin

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
    # 127.0.0.1:8000/post/1/delete --> local
    # mydjangosite.com/post/1/delete--> online
    path('post/<int:pk>/delete/', views.postDelete, name='postDelete'),
    # 127.0.0.1:8000/drafts --> local
    # mydjangosite.com/drafts--> online
    path('drafts/', views.postDraftlist, name='postDraftlist'),
    # 127.0.0.1:8000/post/1/publish --> local
    # mydjangosite.com/post/1/publish--> online
    path('post/<int:pk>/publish/', views.postPublish, name='postPublish'),
    # 127.0.0.1:8000/accounts/login --> local
    # mydjangosite.com/accounts/login--> online
    path('accounts/', include('django.contrib.auth.urls')),
    # 127.0.0.1:8000/post/1/comment --> local
    # mydjangosite.com/post/1/comment--> online
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    # 127.0.0.1:8000/comment/1/remove --> local
    # mydjangosite.com/comment/1/remove--> online
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
    # 127.0.0.1:8000/comment/1/approve --> local
    # mydjangosite.com/comment/1/approve--> online
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
       # 127.0.0.1:8000/signup --> local
    # mydjangosite.com/signup--> online
    path('signup/',views.signup, name='signup')
    # path(r'^accounts/login/$', auth_views.LoginView.as_view(template_name='registration/login.html')),
    #path)
    #url('^change-password/$', auth_views.PasswordChangeView.as_view()),
    #^login/$ [name='login']
    #^password_change/$ [name='password_change']
]


#login( request, template_name=`registration/login.html`, redirect_field_name='next', authentication_form=AuthenticationForm, current_app=None, extra_context=None, redirect_authenticated_user=False

