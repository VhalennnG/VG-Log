from django.contrib import admin
from .models import Post
from .forms import BlogAdminForm

class BlogAdmin(admin.ModelAdmin):
  form = BlogAdminForm

# Register your models here.
admin.site.register(Post, BlogAdmin)