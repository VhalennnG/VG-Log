from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):
  posts = Post.objects.all()
  return render(request, 'index.html', {'posts': posts})
  
def post(request, url):
  posts = Post.objects.get(page_url=url) 
  return render(request, 'posts.html', {'posts': posts})
  
def profile(request):
  return render(request, 'profile.html')