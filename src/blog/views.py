from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from blog.models import Post,Comment
from django.http import JsonResponse
from django.core import serializers
# Create your views here.
def post(request,blog_id):
	if request.method=='GET':
		data=get_object_or_404(Post, pk=blog_id)
		serialized_data=serializers.serialize("json",Post.objects.filter(id=blog_id))
		return HttpResponse(serialized_data)
	elif request.method=='DELETE':
		objects = Blog.objects.get(pk=1)
		objects.delete()
		return HttpResponse("<h3>Post is deleted<h3>")
	else:
		#POST /api/v1/post/ - create new post
		return HttpResponse("PUT RECORD")