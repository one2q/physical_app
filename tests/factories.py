import factory

from blog.models import *


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    name = "Test_name"
    text = "test_text"


class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comment

    text = "some text"
    post = factory.SubFactory(PostFactory)
