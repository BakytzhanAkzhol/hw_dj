from tastypie import fields 
from tastypie.resources import ModelResource
from blog.models import Post,Comment
from tastypie.authorization import Authorization



class PostResource(ModelResource):
    class Meta:
        queryset = Post.objects.all()
        resource_name = 'Post'
        fields=['author','title','pub_date']
        allowed_methods = ('get', 'post', 'put','delete', 'patch')
      	filtering={'title': ALL}
      	excludes = ['author', 'title', 'pub_date','upd_date','is_public']
      	always_return_data = True

class CommentResource(ModelResource):
    post = fields.ForeignKey(PostResource, 'post')
    class Meta:
        queryset = Comment.objects.all() 
        resource_name = 'Comment'
        allowed_methods = ('get', 'post', 'put','delete', 'patch')
        filtering={'author': ALL}
        always_return_data = True

       