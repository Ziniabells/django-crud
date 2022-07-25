from django import forms
from .models import Post

class BlogAppForm(forms):
    class Meta:
        model = Post
        fields = [
        "title",
        "description",
        
        ]