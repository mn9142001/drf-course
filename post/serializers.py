from rest_framework import serializers
from .models import Post, Comment
from user.serializers import UserSerializer


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Comment
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True)
    user = UserSerializer()

    class Meta:
        model = Post
        fields = '__all__'
    
    def get_field_names(self, declared_fields, info):
        return super().get_field_names(declared_fields, info) + ['comment_set']