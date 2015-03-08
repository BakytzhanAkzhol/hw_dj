from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from blog.models import Post,Comment
from django.http import JsonResponse

# Create your views here.
def post(request,blog_id):
	data=get_object_or_404(Post, pk=blog_id)
	return HttpResponse(JsonResponse(data))