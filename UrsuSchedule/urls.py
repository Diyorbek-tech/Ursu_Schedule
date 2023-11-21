from django.contrib import admin
from django.urls import path, include

from django.views.static import serve
from django.urls import re_path
from django.conf import settings

urlpatterns = [
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
]
