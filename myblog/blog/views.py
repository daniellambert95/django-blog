from django.shortcuts import render
from django.http import HttpResponse

import git
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from myblog.blog import apps

from .models import Blog

# Create your views here.


def home(request):
    blog_posts = Blog.objects.all()
    context = {"blog_posts": blog_posts}
    return render(request, "blog/home.html", context)

def blog_post(request, id):
    blog = Blog.objects.get(id=id)
    context = {"blog": blog}
    return render(request, "blog/blog_post.html", context)

#Route for the GitHub webhook
@apps.route('/git_update', methods=['POST'])
def git_update():
  repo = git.Repo('./django-blog')
  origin = repo.remotes.origin
  repo.create_head('main', 
  origin.refs.main).set_tracking_branch(origin.refs.main).checkout()
  origin.pull()
  return '', 200

@csrf_exempt
def update(request):
    if request.method == "POST":
        repo = git.Repo("danjlambert95.pythonanywhere.com/") 
        origin = repo.remotes.origin

        origin.pull()

        return HttpResponse("Updated code on PythonAnywhere")
    else:
        return HttpResponse("Couldn't update the code on PythonAnywhere")
