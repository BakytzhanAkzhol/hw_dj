from tastypie import fields 
from tastypie.resources import ModelResource
from blog.models import Post
from blog.models import Comment
from tastypie.authorization import Authorization



class PostResource(ModelResource):
    class Meta:
        queryset = Post.objects.all()
        resource_name = 'Post'
        allowed_methods = ('get', 'post', 'put','delete', 'patch')
      	filtering={'title': ALL}

class CommentResource(ModelResource):
    post = fields.ForeignKey(PostResource, 'post')
    class Meta:
        queryset = Comment.objects.all()
        allowed_methods = ('get', 'post', 'put','delete', 'patch')
        resource_name = 'Comment'