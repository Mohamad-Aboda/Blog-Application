from typing import Callable
from django.db.models.query import RawQuerySet
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


from .models import Category, Post, Comment
from .forms import CommentForm, SearchForm, CreatePostForm, UpdatePostForm, NewUserForm
from .decorators import * 

def home(request):
    allPosts = Post.objects.filter(status = 'published')
    context = {'allPosts':allPosts}
    return render(request, 'blog/home.html', context)




def postDetail(request, post):
    post = get_object_or_404(Post, slug=post, status='published')
    comments = post.comments.filter(status=True)
    auther = request.user 
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            user_comment = comment_form.save(commit=False)
            user_comment.post = post
            user_comment.name = auther
            user_comment.save()
            return redirect('/' + post.slug)
        
    else:
        comment_form = CommentForm()

    context = {'post':post,'comments':comments, 'comment_form':comment_form}
    return render(request, 'blog/postDetail.html', context)




def category_list(request, category):
    category = Post.objects.filter(status = 'published', category__name=category)
    return render(request, 'blog/category_list.html', {'category':category})


def all_categories(request):
    all_categories = Category.objects.exclude(name='default')
    context = {'all_categories':all_categories,}
    return context 


def search(request):
    form = SearchForm()
    q = ''
    results = []
    if 'q' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            q = form.cleaned_data['q']
            results = Post.objects.filter(title__icontains = q)
            
    return render(request, 'blog/search.html', {'form':form, 'results':results })



@login_required(login_url='/login/')
def deletePost(request, pk):
    item = Post.objects.get(pk=pk)
    if request.user == item.auther:
        get_object_or_404(Post, pk=pk).delete()
        return redirect('/')


@login_required(login_url='/login/')
def createPost(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.auther = request.user 
            instance.save()

            return redirect('/')
    
    else:
        form = CreatePostForm()
    return render(request, 'blog/create.html', {'form':form})



@login_required(login_url='/login/')
def updatePost(request, pk):
    item = get_object_or_404(Post, pk=pk)
    if request.user == item.auther and request.method == 'POST':
        form = UpdatePostForm(request.POST,request.FILES,instance = item)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.auther = request.user 
            instance.save()
            return redirect('/')

    else:
        form = UpdatePostForm()
    return render(request, 'blog/update.html', {'form':form, 'item':item})




@unAuth_user
def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save() 
            messages.success(request, 'Registration successful.')
            return redirect('blog:login_user')
        else:
            messages.error(request, 'Unsuccessful registration. Invalid information.')
    
    form = NewUserForm()
    return render(request, 'blog/register.html', {'form':form})


@unAuth_user
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f'You are logged in as {username}.')
                return redirect('blog:home')
            else:
                messages.error(request, 'Invalid username or password!')
        else:
            messages.error(request, 'Invalid username or password!')
    
    form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form':form})


def logout_user(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('/')


