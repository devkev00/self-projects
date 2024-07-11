from django.db import models

# Create your models here.

class Post(models.Model):
  title=models.CharField(max_length=32)
  user=models.CharField(max_length=20)
  content=models.TextField()

class Comment(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE) 
  #Post의 pk값을 받아옴, cascade: post가 삭제되면 댓글도 전부 삭제
  content = models.TextField()