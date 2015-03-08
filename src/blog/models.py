from django.db import models
from django.utils import timezone

class Post(models.Model):
     author= models.CharField(max_length=50)
     title=models.CharField(max_length=100)
     text=models.CharField(max_length=300)
     pub_date=models.DateTimeField(auto_now_add = timezone.now)
     upd_date= models.DateTimeField(auto_now_add = timezone.now)
     is_public=models.BooleanField(default=False)

     def __str__(self):
     	return self.title+" // "+ self.title;