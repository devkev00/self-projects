from django.urls import path
from .views import *

app_name='posts'

urlpatterns = [
  path('/', post_list),
  path('/create', post_create),
  path('/<int:pk>', post_detail),
  path('/<int:pk>/update', post_update),
  path('/<int:pk>/delete', post_delete),
  path('/<int:pk>/comments/create', comment_create),
]

#model이 만들어졌다는 가정 하에
#url 만들고, views에 함수 만들고, template에 html 만들고
#templates 파일은 따로 뺄 수 있음, 경로 수정(settings.py)