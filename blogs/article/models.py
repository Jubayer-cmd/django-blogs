from django.db import models

class Blog(models.Model):
  title = models.CharField(max_length=100)
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  author = models.CharField(max_length=100)
  image = models.CharField(max_length=100)  # Add image field

  def __str__(self):
    return self.title
