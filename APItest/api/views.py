# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import Post, Comment
from api.serializers import PostListSerializer, PostDetailSerializer, \
    CommentCreateSerializer, CommentSerializer


class PostListView(generics.ListCreateAPIView):
    """Вывод списка статей"""
    queryset = Post.objects.all()
    serializer_class = PostListSerializer


class PostDetailView(APIView):
    """Вывод статьи с комментариями"""
    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        serializer = PostDetailSerializer(post)
        return Response(serializer.data)

class CommentCreateView(APIView):
    """Создать комментарий к посту"""
    def post(self, request):
        comment = CommentCreateSerializer(data=request.data)
        if comment.is_valid():
            comment.save()
        return Response(status=201)


class CommentListView(generics.ListAPIView):
    """Список всех комментариев"""
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentNestedView(generics.ListAPIView):
    """Любой коммент со всеми вложенными"""
    def get(self, request, pk):
        comment = Comment.objects.get(id=pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)




