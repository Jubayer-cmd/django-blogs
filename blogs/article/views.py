from django.shortcuts import render, redirect
from django.urls import path
from django.http import HttpResponse
from .models import Blog

# Create your views here.
def my_view(request):
  blogs = Blog.objects.all()
  return render(request, 'home.html', {'blogs': blogs})

def post_blogs(request):
  if request.method == 'POST':
    title = request.POST.get('title')
    content = request.POST.get('content')
    author = request.POST.get('author')
    image = request.POST.get('image')

    blog = Blog(title=title, content=content, author=author, image=image)
    blog.save()

    return redirect('/')  # Replace 'home' with the appropriate URL name for the home page

  return render(request, 'postBlogs.html')

def blog_details(request, blog_id):
  blog = Blog.objects.get(id=blog_id)
  return render(request, 'detail.html', {'blog': blog})
