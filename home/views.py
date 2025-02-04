from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home/index.html')


def about(request):
    return render(request, 'home/about.html')


def impressum(request):
    return render(request, 'home/impressum.html')


def post_list(request):
    """REQUESTS POSTS"""
    posts = Post.objects.filter(
        published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'home/post_list.html', {'posts': posts})


def post_detail(request, pk):
    """REQUESTS FULL POST"""
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'home/post_detail.html', {'post': post})


@login_required
def post_new(request):
    """WRITE NEW POST"""
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'home/post_edit.html', {'form': form})


@login_required
def post_edit(request, pk):
    """EDIT POST"""
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'home/post_edit.html', {'form': form})
