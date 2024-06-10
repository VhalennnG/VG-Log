from django.db import models
from datetime import datetime

# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=100, default="Title Post")
  page_url = models.CharField(max_length=100, blank=False)
  thumbnail = models.ImageField(upload_to='posts/images/thumbnails', default='posts/images/thumbnails/null.jpg')
  body = models.TextField(blank=False)
  pub_date = models.DateTimeField(default=datetime.now , blank=True)
  
  def __str__(self):
    return self.title