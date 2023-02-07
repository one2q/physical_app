from rest_framework import serializers
from blog.models import *


class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["pk", "text"]


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["pk", "text", "post"]


class PostListSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["comments"] = CommentListSerializer(instance.comments.first()).data
        return representation

    class Meta:
        model = Post
        fields = "__all__"


class PostDetailSerializer(serializers.ModelSerializer):
    comments = CommentListSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = "__all__"
