from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Category, Thread, Post
from .forms import ThreadForm, PostForm, UserRegistrationForm


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('category_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'forum/category_list.html', {'categories': categories})


def thread_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    threads = category.threads.filter(is_published=True)
    return render(request, 'forum/thread_list.html', {'category': category, 'threads': threads})


def thread_detail(request, category_slug, thread_slug):
    thread = get_object_or_404(
        Thread, slug=thread_slug, category__slug=category_slug, is_published=True)
    posts = thread.posts.filter(is_approved=True)
    return render(request, 'forum/thread_detail.html', {'thread': thread, 'posts': posts})


@login_required
def new_thread(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    if request.method == 'POST':
        form = ThreadForm(request.POST)
        if form.is_valid():
            thread = form.save(commit=False)
            thread.category = category
            thread.author = request.user
            thread.save()
            return redirect('thread_detail', category_slug=category.slug, thread_slug=thread.slug)
    else:
        form = ThreadForm()
    return render(request, 'forum/new_thread.html', {'form': form})


@login_required
def new_post(request, category_slug, thread_slug):
    thread = get_object_or_404(
        Thread, slug=thread_slug, category__slug=category_slug)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.thread = thread
            post.author = request.user
            post.save()
            return redirect('thread_detail', category_slug=category.slug, thread_slug=thread.slug)
    else:
        form = PostForm()
    return render(request, 'forum/new_post.html', {'form': form})