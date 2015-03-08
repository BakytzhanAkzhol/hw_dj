from django.db import models
from django.utils import timezone

class Post(models.Model):
     author=models.CharField(max_length=100)
     title=models.CharField(max_length=100)
     text=models.CharField(max_length=300)
     pub_date= models.DateTimeField(default=timezone.now)
     upd_date=  models.DateTimeField(default=timezone.now)
     is_public=models.BooleanField(default=True)

     def __str__(self):
     	return self.title;

class Comment(models.Model):
	author=models.CharField(max_length=100)
	text=models.CharField(max_length=300)
	pub_date=models.DateTimeField(default=timezone.now)
	post = models.ForeignKey(Post, related_query_name="fk")

	def __str__(self):
		return self.text