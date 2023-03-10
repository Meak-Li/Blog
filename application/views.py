from django.shortcuts import render, get_object_or_404
from application.models import Post

def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'static/blog/index.html', context={'post_list': post_list})

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'static/blog/detail.html', context={'post': post})