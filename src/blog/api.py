from tastypie import fields 
from tastypie.resources import ModelResource
from blog.models import Post
from blog.models import Comment
from tastypie.authorization import Authorization

class PostResource(ModelResource):
    author = fields.CharField(attribute="author")
    title = fields.CharField(attribute="title")
    text = fields.CharField(attribute="text")
    comments = fields.ToManyField('blog.api.CommentResource', 'comment_set', null=True)

    class Meta:
        queryset = Post.objects.all()
        resource_name = 'post'
        authorization = Authorization()
        always_return_data = True

class CommentResource(ModelResource):
    author = fields.CharField(attribute="author")
    text = fields.CharField(attribute="text")   
    post = fields.ForeignKey(PostResource, 'post')
    post = fields.ToOneField('blog.api.PostResource', 'post')

    class Meta:
        queryset = Comment.objects.all()
        resource_name = 'comment'
        authorization = Authorization()
        always_return_data = True
