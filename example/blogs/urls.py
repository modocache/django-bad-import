from django.conf.urls import patterns, url

from blogs.views.blogs import BlogListView, BlogDetailView
from blogs.views.posts import PostDetailView


urlpatterns = patterns('',
    url(
        regex=r'^$',
        view=BlogListView.as_view(),
        name='blog_list'
    ),
    url(
        regex=r'^(?P<blog_pk>\d+?)$',
        view=BlogDetailView.as_view(),
        name='blog_detail'
    ),

    url(
        regex=r'^(?P<blog_pk>\d+?)/(?P<post_pk>\d+?)$',
        view=PostDetailView.as_view(),
        name='post_detail'
    ),
)
