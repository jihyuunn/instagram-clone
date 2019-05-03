from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import CommentForm, PostForm

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts':posts})

def detail(request, post_pk):
    thispost = Post.objects.get(pk=post_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        comment = form.save(commit=False)
        comment.post = thispost
        comment.save()
        return redirect('detail', post_pk)
    else:
        form = CommentForm()
    return render(request, 'detail.html', {'thispost':thispost, 'form':form})

def new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        post = form.save(commit=False)
        form.save()
        return redirect('detail', post.pk)
    else:
        form = PostForm()
    return render(request, 'new.html', {'form':form})