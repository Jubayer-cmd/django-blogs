from django.urls import path
from .views import my_view, post_blogs, blog_details

urlpatterns = [
  path('', my_view, name='my_view'),
  path('post_blogs/', post_blogs, name='post_blogs'),
  path('blog/<int:blog_id>/', blog_details, name='blog_details'),
]
