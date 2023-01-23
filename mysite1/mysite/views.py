# function file
from django.shortcuts import render
from django.http import HttpResponse
from mysite.models import Post, Like
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.contrib.auth.models import User


def index(request):
    posts = Post.objects.all()

    postLikeArray = []

    # a for loop where we go through each of the items in the posts queryset and
    # input the actual post object into the aray
    i = 0
    for post in posts:
        likes = Like.objects.filter(post=post)
        mylist = [post, likes]
        postLikeArray.append(mylist)
        i = i + 1


# Inside the first loop (per post), we look for all of the likes that are associated with that post and
    # add to the second
    template_variables = {
        'foo': 'bar',
        'username': 'hanna',
        'postLikeArray': postLikeArray
    }
    return render(request, "index.html", context=template_variables)
    # return HttpResponse("Hello, world!")


def test_i(i, mylist, post):
    i = mylist.count(post)


@api_view(['GET', 'POST'])
@csrf_exempt
def masterendpoint(request):
    # figure out the request type
    # if type is create post, then create a new post and save to db
    if request.data.get("type") == "newpost":
        title = request.data.get("title")
        author = User.objects.filter(
            username=request.data.get("username")).first()
        content = request.data.get("content")
        newpost = Post.objects.create(
            author=author, title=title, content=content)
        newpost.save()
        return HttpResponse()
    template_variables = {
        'foo': 'bar',
        'username': 'hanna1',
        'email': 'test1@test.com'
    }

    # return render(request, "index.html", context=template_variables)
    if request.data.get("username") is None:
        return HttpResponse("No User")
    else:
        return HttpResponse(User.objects.filter(
            username=request.data.get("username")).first().email)
