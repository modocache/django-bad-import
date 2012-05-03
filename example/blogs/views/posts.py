from django.shortcuts import get_object_or_404
from django.views.generic import DetailView

from example.blogs.models import Post


class  PostDetailView(DetailView):
    model = Post

    def get_object(self):
        blog_pk = self.kwargs.get('blog_pk')
        post_pk = self.kwargs.get('post_pk')
        return get_object_or_404(
            self.model.objects, blog__pk=blog_pk, pk=post_pk)
