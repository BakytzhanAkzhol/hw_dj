from tastypie import fields 
from tastypie.resources import ModelResource
from blog.models import Post
from blog.models import Comment
from tastypie.authorization import Authorization



class PostResource(ModelResource):
    class Meta:
        queryset = Post.objects.all()
        resource_name = 'post'
        authorization = Authorization()
        always_return_data = True

class CommentResource(ModelResource):
    post = fields.ForeignKey(PostResource, 'post')
    class Meta:
        queryset = Comment.objects.all()
        resource_name = 'comment'
        authorization = Authorization()
        always_return_data = True