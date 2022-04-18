from rest_framework import serializers

from .models import Post, Comment


class FilterCommentListSerializer(serializers.ListSerializer):
    """фильтр для комментариев родителя"""
    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecursiveSerializer(serializers.Serializer):
    """Вложенность отзывов"""
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class CommentCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    """Вывод отзыва"""

    children = RecursiveSerializer(many=True)

    class Meta:
        list_serializer_class = FilterCommentListSerializer
        model = Comment
        fields = ['id', 'parent', 'post', 'name', 'text', 'level', 'children']


class PostDetailSerializer(serializers.ModelSerializer):
    """Полный пост"""
    comment = CommentSerializer(many=True)

    class Meta:
        model = Post
        fields = '__all__'


class PostListSerializer(serializers.ModelSerializer):
    """список постов"""
    class Meta:
        model = Post
        fields = '__all__'
