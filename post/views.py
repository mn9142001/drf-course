from .models import Post, Comment
from django.http import JsonResponse
from .serializers import PostSerializer
from django.db.models import Prefetch

def posts_list(request):
    posts = Post.objects.all()
    posts_serializer = PostSerializer(posts, many=True)
    return JsonResponse({"posts" : posts_serializer.data})