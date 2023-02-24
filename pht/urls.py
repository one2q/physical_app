from django.contrib import admin
from django.urls import path, include

from blog.urls import blog_router
from blog.yasg import urlpatterns as doc_urls
from pht import settings

urlpatterns = [
	path("admin/", admin.site.urls),
	path("api/", include(blog_router.urls)),

]

urlpatterns += doc_urls

if settings.DEBUG:
	urlpatterns += [path('__debug__/', include('debug_toolbar.urls')), ]
