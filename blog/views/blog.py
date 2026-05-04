from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from blog.models.blog import Post
from blog.serializers.blog import PostCreateSerializer, PostModelSerializer


@api_view(["GET"])
def home(request: Request):
    posts = Post.objects.all().order_by("-created_at")
    serializer = PostModelSerializer(posts, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_blog(request: Request):
    serializer = PostCreateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    # save post
    post = serializer.save(author=request.user) 

    serializer = PostModelSerializer(post)

    return Response(data=serializer.data, status=status.HTTP_201_CREATED)

@api_view(["POST"])
def update_blog(request: Request):
    pass

@api_view(["POST"])
def delete_blog(request: Request):
    pass