from django.contrib import admin
from django.urls import path, include

from blog.urls import blog_router
from blog.yasg import urlpatterns as doc_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(blog_router.urls)),
]

urlpatterns += doc_urls