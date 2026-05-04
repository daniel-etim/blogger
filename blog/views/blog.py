from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.request import Request
from rest_framework.response import Response

from blog.models.blog import Post
from blog.serializers.blog import PostCreateSerializer, PostDetailSerializer, PostListSerializer, PostModelSerializer, PostUpdateSerializer


@api_view(["GET"])
def home(request: Request):
    posts = Post.objects.all().order_by("-created_at")
    serializer = PostModelSerializer(posts, many=True)
    return Response(data=serializer.data, status=status.HTTP_200_OK)

@api_view(["GET"])
@permission_classes([IsAuthenticatedOrReadOnly])
def post_list(request: Request):
    posts = Post.objects.all().order_by("-created_at")
    serializer = PostListSerializer(posts, many=True)

    return Response(data=serializer.data, status=status.HTTP_200_OK)

@api_view(["GET"])
@permission_classes([IsAuthenticatedOrReadOnly])
def post_detail(request: Request, pk: int):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(data={"error": "Post Not Found"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = PostDetailSerializer(post)
    
    return Response(data=serializer.data, status=status.HTTP_200_OK)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_post(request: Request):
    serializer = PostCreateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    # save post
    post = serializer.save(author=request.user) 

    serializer = PostModelSerializer(post)

    return Response(data=serializer.data, status=status.HTTP_201_CREATED)

@api_view(["PUT", "PATCH"])
@permission_classes([IsAuthenticated])
def update_post(request: Request, pk: int):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(data={"error": "Post Not Found"}, status=status.HTTP_400_BAD_REQUEST)
    
    if post.author != request.user:
        return Response(data={"error": "You're not authorized to edit this post"}, status=status.HTTP_401_UNAUTHORIZED)
    
    serializer = PostUpdateSerializer(post, data=request.data, partial=True)

    serializer.is_valid(raise_exception=True)

    serializer.save()

    return Response(data=("Success", serializer.data), )

@api_view(["POST"])
def delete_post(request: Request):
    pass