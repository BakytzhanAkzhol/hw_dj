from django.contrib import admin
from blog.models import Post

# Register your models here.
 

class PostAdmin(admin.ModelAdmin):
	fieldsets = [
        (None,               {'fields': ['title']}),
        (None, {'fields': ['author','text','is_public'],}),
    ]
      #  ('Date',{'fields':['pub_date','upd_date']})	

admin.site.register(Post,PostAdmin)