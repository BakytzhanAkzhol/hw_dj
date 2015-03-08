from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from blog.models import Post,Comment
from django.http import JsonResponse
from django.core import serializers
from django.utils import timezone
# Create your views here.
def post(request,blog_id):
	if request.method=='GET':
		data=Post.objects.filter(id=blog_id)
		comments=Comment.objects.filter(post=blog_id)
		serialized_data=serializers.serialize("json",data)
		serialized_comments=serializers.serialize("json",comments)
		return JsonResponse({'post':serialized_data,'comments':serialized_comments})
	elif request.method=='DELETE':
		objects = Blog.objects.get(pk=blog_id)
		objects.delete()
		return HttpResponse("<h3>Post is deleted<h3>")
	elif request.method=='PATCH':
		#Po idea, doljno rabotat. 4erez, Postman vivodit owibku 403
		data=Post.objects.filter(id=blog_id)
		data.author=request.POST['author']
		data.title=request.POST['title']
		data.upd_date=timezone.now
		data.save();
		return HttpResponse("Post edited successsfully")