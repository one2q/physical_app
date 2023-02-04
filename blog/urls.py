from rest_framework import routers
from blog.views import *

blog_router = routers.SimpleRouter()
blog_router.register("post", PostViewSet)
blog_router.register("comment", CommentViewSet)
