from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    # load all the post from db(10)
    posts=Post.objects.all()
    cats=Category.objects.all()
    return render(request,"home.html",{'posts':posts,'cats':cats})

def post(request,url):
    post=Post.objects.get(url=url)
    print(post)
    cats=Category.objects.all()
    return render(request,'posts.html',{'post':post,'cats':cats})

def category(request,url):
    # the below code is used for parent child hierarchy.
    cat=Category.objects.get(url=url)
    posts=Post.objects.filter(cat=cat)
    return render(request,"category.html",{'cat':cat,'posts':posts})