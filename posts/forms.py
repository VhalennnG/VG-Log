from django import forms
from .models import Post

class BlogAdminForm(forms.ModelForm):
  body = forms.CharField(widget=forms.Textarea(attrs={'id': "richtext_field"}))
  
  class Meta:
    model = Post
    fields = "__all__"