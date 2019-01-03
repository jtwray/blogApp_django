from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .forms import PostForm, CommentForm, UserForm
from .models import Post, Comment


# Create your views here.
def postsList(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    stuff_for_frontend = {'posts': posts}
    return render(request, 'blog/postsList.html', stuff_for_frontend)

def postsDetail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    stuff_for_frontend = {'post': post}
    return render(request, 'blog/postsDetail.html', stuff_for_frontend)

@login_required
def postNew(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('postsDetail', pk=post.pk)
    else:
        form = PostForm()
        stuff_for_frontend = {'form': form}
    return render(request, 'blog/postEdit.html', stuff_for_frontend)

@login_required
def postEdit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        # updating an existing form
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('postsDetail', pk=post.pk)
    else:
        form = PostForm(instance=post)
        stuff_for_frontend = {'form': form, 'post':post}
    return render(request, 'blog/postEdit.html', stuff_for_frontend)

@login_required
def postDraftlist(request):
         posts = Post.objects.filter(published_date__isnull=True).order_by('-created_date')
         stuff_for_frontend = {'posts': posts}
         return render(request, 'blog/postDraftlist.html', stuff_for_frontend)   

@login_required        
def postPublish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('postsDetail', pk=pk)

@login_required
def postDelete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('postsList')

@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('/', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})
@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('postsDetail', pk=comment.post.pk)
@login_required
def comment_approve(request,pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return  redirect('postsDetail', pk=comment.post.pk)

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            new_user =  User.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            return redirect('/')
    else:
        form = UserForm()
    return render(request, 'blog/signup.html', {'form': form})    