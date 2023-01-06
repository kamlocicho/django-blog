from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.urls import reverse
from .forms import PostForm
from .models import Post

# Create your views here.
def home(request):
    posts = Post.objects.all()

    if request.method == 'POST':
        id = request.POST['delete']
        post = Post.objects.filter(id=id).first()
        
        if post and (post.author == request.user or request.user.has_perm('posts.delete_post')):
            post.delete()

        return render(request, 'posts/home.html', {"posts": posts})

    return render(request, 'posts/home.html', {"posts": posts})

@login_required(login_url=settings.LOGIN_URL)
def createPost(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect(reverse('home'))
        return render(request, 'posts/create-post.html', {"form": form})
    else:
        form = PostForm()
        return render(request, 'posts/create-post.html', {"form": form})