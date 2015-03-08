from django.contrib import admin
from blog.models import Post
from blog.models import Comment

# Register your models here.
 

class PostAdmin(admin.ModelAdmin):
	fieldsets = [
        (None,               {'fields': ['title']}),
        (None, {'fields': ['author','text','is_public']}),
        ('Published', {'fields': ['pub_date']}),
         ('Update time', {'fields': ['upd_date']}),
    ]
class CommentAdmin(admin.ModelAdmin):
	fieldsets=[('Post',{'fields':['post']}),
	('Text',{'fields':['text','pub_date']}),
	]
      #  ('Date',{'fields':['pub_date','upd_date']})	

admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)