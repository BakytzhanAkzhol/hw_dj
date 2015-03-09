from django.conf.urls import patterns, include, url
from django.contrib import admin
from tastypie.api import Api
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from blog.api import PostResource,CommentResource
from blog import views

post=PostResource()
comment=CommentResource()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hw002.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/',include(comment.urls)),
    url(r'^api/v1/',include(post.urls)),
    url(r'^api/v1/post/(?P<blog_id>\d+)/$', views.post, name='detail'),
)
