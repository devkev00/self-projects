from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Post, Comment

# Create your views here.
def post_list(request):
  # return HttpResponse('안녕하세요')
  posts=Post.objects.all()
  context={
    "posts":posts
  }
  return render(request, 'post_list.html', context)

def post_create(request):
  if request.method=="POST":
    Post.objects.create( # create의 경우는 알아서 db에 insert를 해줌
      title=request.POST["title"],
      user=request.POST["user"],
      content=request.POST["content"]
      )
    return redirect("/posts")
  return render(request, 'post_create.html')

def post_detail(request, pk):
  post=Post.objects.get(id=pk)

  previous_id = Post.objects.filter(id__lt=pk).order_by("-id")[0].pk
  next_id = Post.objects.filter(id__gt=pk).order_by("id")[0].pk
  comments = Comment.objects.filter(post=pk)

  context = {
    "post":post,
    "previous_post_id":previous_id,
    "next_post_id":next_id,
    "comments": comments
  }
  return render(request, 'post_detail.html', context)

def post_update(request, pk):
  post=Post.objects.get(id=pk)
  if request.method == "POST":
    post.title = request.POST["title"]
    post.user = request.POST["user"]
    post.content = request.POST["content"]

    post.save() # 중요, 기존 db에 접근해서 값을 바꾸는 것이기 때문에 저장을 해주는 것임

    return redirect(f"/posts/{pk}")

  context = {
    "post":post
  }
  return render(request, 'post_update.html', context)

def post_delete(request, pk):
  if request.method == "POST":
    post=Post.objects.get(id=pk)
    post.delete()
  return redirect("/posts")

def comment_create(request, pk):
  if request.method == "POST":
    post=Post.objects.get(id=pk)
    Comment.objects.create(
      post=post,
      content = request.POST["content"]
    )

  return redirect(f"/posts/{pk}")