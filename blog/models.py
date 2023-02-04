from django.db import models


class Post(models.Model):
	name = models.CharField(max_length=63)
	text = models.CharField(max_length=2000)
	view_count = models.IntegerField(default=0)
	created_at = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.name


class Comment(models.Model):
	text = models.CharField(max_length=2000)
	created_at = models.DateField(auto_now_add=True)
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

	def __str__(self):
		return self.text

