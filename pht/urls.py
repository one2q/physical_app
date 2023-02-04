from django.contrib import admin
from django.urls import path

from blog.urls import blog_router

urlpatterns = [
    path("admin/", admin.site.urls),
]

urlpatterns += blog_router.urls
