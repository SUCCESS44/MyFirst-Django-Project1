from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def post_list(request):
    object_list = Post.published.all()# to retrieve the post from db
    paginator = Paginator(object_list, 9)
    page = request.GET.get('page') # Get is a class, get is a method inside the class
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)        
    return render(request, "blog/post/list.html", {"posts": posts}) #render: takes a request,a path to the template and the context
def post_detail(request, year, month, day, post):
    post = get_object_or_404(post ,slug=post, status="published", publish__year=year, publish__month=month, publish__day=day)
    return render(request, "blog/post/detail.html", {"post": post})