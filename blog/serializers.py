from rest_framework import serializers
from blog.models import *


class CommentListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Comment
		fields = ["pk", "text"]


class PostListSerializer(serializers.ModelSerializer):
	comments = CommentListSerializer(many=True, read_only=True)  #TODO можно и без этого поля, убрать?

	def to_representation(self, instance):
		representation = super().to_representation(instance)
		if instance.comments.exists():
			comment = instance.comments.all().order_by('-pk').first()
			representation['comments'] = CommentListSerializer(comment).data
		else:
			representation['comments'] = None
		return representation

	class Meta:
		model = Post
		fields = '__all__'


class PostDetailSerializer(serializers.ModelSerializer):
	comments = CommentListSerializer(many=True, read_only=True)

	class Meta:
		model = Post
		fields = '__all__'