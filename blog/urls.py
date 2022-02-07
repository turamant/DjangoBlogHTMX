from django.urls import path

from blog.views import create, blog, home, preview

urlpatterns = [
    path("", home, name="home"),
    path("create/", create, name="create"),
    path("preview/", preview, name="preview"),
    path("blog/<slug:slug>/", blog, name="blog"),
]