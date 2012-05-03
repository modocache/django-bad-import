from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from example.blogs.models import Blog


class BlogListView(ListView):
    model = Blog

    def get_queryset(self):
        return self.model.objects.all()


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self):
        blog_pk = self.kwargs.get('blog_pk')
        return get_object_or_404(self.model.objects, pk=blog_pk)
