import markdown
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from .forms import BlogForm
from .models import Blog


def home(request):
    blogs = Blog.objects.all()
    return render(request, "home.html", {"blogs": blogs})

def blog(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    content = markdown.markdown(blog.content)
    return render(request, "blog.html", {"content": content, "title": blog.title})

def create(request):
    form = BlogForm()
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save()
            return redirect("/")
        else:
            return render(request, "create_blog.html", {"form": form, "errors": form.errors})
    return render(request, "create_blog.html", {"form": form, "errors": None})

def preview(request):
    content = markdown.markdown(request.POST["content"])
    return HttpResponse(content)
