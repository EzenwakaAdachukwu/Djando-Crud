from audioop import reverse
from dataclasses import field
from msilib.schema import ListView
from django.shortcuts import render

from I4G008611FZU.blog.models import Post

# Create your views here.
class PostListView(ListView):
    model=Post

class PostCreateView(CreateView):
    model = Post
    field="____all____"
    success-url =reverse_lazy("blog:all")

class PostDetailView(DetailView):
    model =Post 


class PostUpdateView(UpdateView):
    model =Post
    field="____all____"
    success-url =reverse_lazy("blog:all") 


class PostDeleteView(DeleteView):
    model =Post
    field="____all____"
    success-url =reverse_lazy("blog:all")        
