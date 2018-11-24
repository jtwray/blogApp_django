from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
# Create your views here.
def postsList(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    stuff_for_frontend = {'posts': posts}
    return render(request, 'blog/postsList.html', stuff_for_frontend)

def postsDetail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    stuff_for_frontend = {'post': post}
    return render(request, 'blog/postsdetail.html', stuff_for_frontend)
