from rest_framework import serializers

from blog.models.blog import Post
from user.models.user import User
from user.serializers.user import UserModelSerializer


class PostModelSerializer(serializers.ModelSerializer):
    author = UserModelSerializer()
    class Meta:
        model = Post
        fields = "__all__"

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["title", "body", "slug"]
