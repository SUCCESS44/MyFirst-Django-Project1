from os import lseek
from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.published.all()# to retrieve the post from db
    return render(request, "blog/post/list.html", {"posts": posts}) #render: takes a request,a path to the template and the context
def post_detail(request, year, month, day, post):
    post = get_object_or_404(post ,slug=post, status="published", publish__year=year, publish__month=month, publish__day=day)
    return render(request, "blog/post/detail.html", {"post": post})