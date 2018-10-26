from .models import Post
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy


# Create your views here.


class PostListView(ListView):
    model = Post
    template_name = 'posts/post_list.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_details.html'


class PostUpdateView(UpdateView):
    model = Post
    fields = [
        'title',
        'content',
        'author',
        'publish_date'
    ]
    template_name = 'posts/post_update.html'


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'posts/post_delete'
    success_url = reverse_lazy('post_list.html')


class PostCreateView(CreateView):
    model = Post
    fields = [
        'title',
        'content',
        'author',
    ]
    template_name = 'posts/post_create.html'
    success_url = reverse_lazy('post_list.html')
