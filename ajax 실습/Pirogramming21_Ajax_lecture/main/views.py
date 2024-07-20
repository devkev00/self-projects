from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

# Create your views here.


def post_list(request):
    posts = Post.objects.all()
    ctx = {
        'posts': posts,
    }
    return render(request, 'main/post_list.html', ctx)


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:post_list')
        else:
            ctx = {
                'form': form,
            }
            return render(request, 'main/post_new.html', ctx)
    elif request.method == 'GET':
        form = PostForm()
        ctx = {
            'form': form,
        }
        return render(request, 'main/post_new.html', ctx)


from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

@csrf_exempt # csrf 적용 안하겠다, 보안상 체크 안하겠다! -> 보안상 문제 없긴 함(django가 기본설정에 넣어놓음)
def like_ajax(request):
    req = json.loads(request.body)
    post_id = req['id']
    button_type = req['type']

    post = Post.objects.get(id=post_id)

    if button_type == 'like':
        post.like += 1
    else:
        post.dislike += 1

    post.save()

    return JsonResponse({'id': post_id, 'type': button_type})