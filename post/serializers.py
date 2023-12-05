from rest_framework import serializers
from .models import Post, Comment
from user.serializers import UserSerializer

from rest_framework.exceptions import  ValidationError

class CustomSeriliazer(serializers.Serializer):
    even_int = serializers.IntegerField()
    extra_int = serializers.IntegerField()

    def validate_even_int(self, value):
        if (value % 2) == 0:
            return value
        raise ValidationError(detail="is not an even number")
    
    def validate(self, attrs : dict):
        if attrs['even_int'] + attrs['extra_int'] == 10:
            return attrs

        raise ValidationError("sum two integers is not 10")


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Comment
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)
    create_user = serializers.HiddenField(default=serializers.CurrentUserDefault(), source="user")

    class Meta:
        model = Post
        fields = '__all__'
    
    def get_field_names(self, declared_fields, info):
        return super().get_field_names(declared_fields, info) + ['comment_set']
    
    