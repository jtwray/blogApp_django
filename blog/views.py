from django.shortcuts import render
from django.utils import timezone
from .models import Post
# Create your views here.
def postsList(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    stuff_for_frontend = {'posts': posts}
    return render(request, 'blog/postsList.html', stuff_for_frontend)
