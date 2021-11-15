import yfinance as yf
import git

# Django
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Models
from .models import Blog
from .models import Post

# Create your views here.


def home(request):
    blog_posts = Blog.objects.all()
    context = {"blog_posts": blog_posts}
    return render(request, "blog/home.html", context)

def blog_post(request, id):
    blog = Blog.objects.get(id=id)
    context = {"blog": blog}
    return render(request, "blog/blog_post.html", context)

def post(request, id):
    post = Post.objects.get(id=id)
    context = {"post": post}
    return render(request, "blog/post.html", context)

def stock_page(request):
    stock_lander = Blog.objects.all()
    context = {"stock_lander": stock_lander}
    return render(request, "blog/stock_api.html", context)

def stock_info(request, ticker_symbol):
    ticker_info = yf.Ticker(ticker_symbol).info
    context = {"ticker_info": ticker_info}
    print(ticker_info)
    return render(request, "blog/stock_api.html", ticker_info)

def main_view(request):
    return render(request, "blog/graph.html", {})


@csrf_exempt
def update(request):
    if request.method == "POST":
        repo = git.Repo("django-blog/") 
        origin = repo.remotes.origin

        origin.pull()

        return HttpResponse("Updated code on PythonAnywhere")
    else:
        return HttpResponse("Couldn't update the code on PythonAnywhere")
