from django.contrib import admin
from polls.models import Question
# Register your models here.

admin.site.register(Question)

class QuestionAdmin(admin.ModelAdmin):
	list_display = ('question_text', 'pub_date')
