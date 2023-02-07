from django.db.models import F
from rest_framework.viewsets import ModelViewSet
from blog.serializers import *
from blog.models import Post, Comment


class PostViewSet(ModelViewSet):
	queryset = Post.objects.all().prefetch_related("comments")
	serializer_classes = {"retrieve": PostDetailSerializer, "list": PostListSerializer}

	def get_serializer_class(self):
		return self.serializer_classes.get(self.action, PostDetailSerializer)

	def retrieve(self, request, *args, **kwargs):
		Post.objects.update(view_count=F("view_count") + 1)
		return super().retrieve(request, *args, **kwargs)


class CommentViewSet(ModelViewSet):
	queryset = Comment.objects.all()
	serializer_classes = {
		"create": CommentCreateSerializer,
		"list": CommentListSerializer,
	}

	def get_serializer_class(self):
		return self.serializer_classes.get(self.action, CommentListSerializer)
