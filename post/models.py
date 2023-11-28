from django.db import models

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey('user.User', models.CASCADE)
    body = models.TextField(max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    user = models.ForeignKey('user.User', models.CASCADE)
    post = models.ForeignKey("post.Post", models.CASCADE)

    reply_to = models.ForeignKey('self', models.CASCADE, blank=True, null=True)

    body = models.TextField(max_length=512)
    created_at = models.DateTimeField(auto_now_add=True)

