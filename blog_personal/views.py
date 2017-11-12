from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .models import Post
# Create your views here.
def index(request):
    return render (request,'index.html',{})
def post_list(request):
    object_list = Post.published.all()
    paginator = Paginator(object_list,5)
    page = request.GET.get('page', 1)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render (request,'blog.html',{'page': page ,'posts':posts})


def post_detail (request,year,month,day,post):
    post = get_object_or_404(Post,slug=post,
                                  status ='published',
                                  publish__year = year,
                                  publish__month = month,
                                  publish__day = day)
    return render(request,'post.html',{'post':post})