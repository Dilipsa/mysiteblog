from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .forms import PostForm
from .models import Post, BlogComment


def post_list(request):
    post = Post.objects.all()
    comments = BlogComment.objects.filter(post=post)
    context = {
        'post': post,
        'comments': comments
    }
    return render(request, 'post_list.html', context)


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    # post = Post.objects.filter(slug=slug).first()
    comments = BlogComment.objects.filter(post=post, parent=None).order_by("-sno")
    replies = BlogComment.objects.filter(post=post).exclude(parent=None).order_by("-sno")
    replyDict = {}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno] = [reply]
        else:
            replyDict[reply.parent.sno].append(reply)
    context = {'post': post,
               'comments': comments,
               'replyDict': replyDict,
               # 'slug': slug
               }
    print(replyDict)
    return render(request, 'post_detail.html', context)


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog:post_detail', slug=post.slug)
    else:
        form = PostForm()
    return render(request, 'post_edit.html', {'form': form})


def post_edit(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = BlogComment.objects.filter(post=post)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog:post_detail', slug=post.slug)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form})


def postComment(request, slug):
    if request.method == "POST":
        comment = request.POST.get("comment")
        postSno = request.POST.get("postSno")
        parentSno = request.POST.get("parentSno")
        user = request.user

        post = Post.objects.get(sno=postSno)

        if parentSno == "":
            comment = BlogComment(comment=comment, user=user, post=post)
            comment.save()
            messages.success(request, "Your comment has been posted successfully")

        else:
            parent = BlogComment.objects.get(sno=parentSno)
            comment = BlogComment(comment=comment, user=user, post=post, parent=parent)
            comment.save()
            messages.success(request, "Your reply has been posted successfully")
        return redirect('/')
