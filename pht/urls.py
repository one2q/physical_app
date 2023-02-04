from django.contrib import admin
from django.urls import path

from blog.urls import blog_router
from blog.yasg import urlpatterns as doc_urls

urlpatterns = [
    path("admin/", admin.site.urls),
]

urlpatterns += blog_router.urls
urlpatterns += doc_urls