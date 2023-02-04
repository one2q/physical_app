from rest_framework.viewsets import ModelViewSet
from blog.serializers import *
from blog.models import *


class PostViewSet(ModelViewSet):
	queryset = Post.objects.all().prefetch_related('comments')
	serializer_classes = {
		'retrieve': PostDetailSerializer,
		'list': PostListSerializer
	}

	def get_serializer_class(self):
		return self.serializer_classes.get(self.action, PostDetailSerializer)

	def retrieve(self, request, *args, **kwargs):
		instance = self.get_object()
		instance.view_count += 1
		instance.save()
		return super().retrieve(request, *args, **kwargs)


class CommentViewSet(ModelViewSet):
	serializer_class = CommentListSerializer
	queryset = Comment.objects.all()
