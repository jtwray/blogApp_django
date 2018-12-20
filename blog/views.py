from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .forms import PostForm, CommentForm
from .models import Post


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
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('postsDetail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form':form})
